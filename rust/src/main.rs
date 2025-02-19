use dotenv::dotenv;
use reqwest::{self, header::{AUTHORIZATION, CONTENT_TYPE, ACCEPT}};
use std::env;
use std::fs::File;
use std::io::Write;

fn write_file(response: Result<String, reqwest::Error>, export_path: String) {
    match response {
        Ok(response) => {
            match File::create(&export_path) {
                Ok(mut file) => {
                    let text = response.as_bytes();
                    if let Err(e) = file.write_all(text) {
                        eprintln!("Failed to write file: {}", e);
                    }
                }
                Err(e) => eprintln!("Failed to create file: {}", e),
            }
            println!("Writing to file: {}", &export_path);
        }
        Err(e) => eprintln!("Error: {}", e),
    }
}

#[tokio::main]
async fn main() {
    dotenv().ok();

    let api_key = env::var("API_KEY").unwrap_or_else(|_| "".to_string());
    let user_id = env::var("USER_ID").unwrap_or_else(|_| "".to_string());
    let export_format = env::var("EXPORT_FORMAT").unwrap_or_else(|_| "".to_string()); 
    let export_path = env::var("EXPORT_PATH").unwrap_or_else(|_| "".to_string());

    let url = format!("https://api.zotero.org/users/{}/items/top?format={}", user_id, export_format);
    let response = reqwest::Client::new()
        .get(&url)
        .header(AUTHORIZATION, format!("Bearer {}", &api_key))
        .header(CONTENT_TYPE, "application/json")
        .header(ACCEPT, "application/json")
        .send()
        .await
        .unwrap()
        .text()
        .await;

    write_file(response, export_path);
}
