--- --> Nicht eingetragen
title: "Teilgebiete Rechnerarchitektur"
date: 25.02.2025
tags: "bachelor"
---

# Teilgebiete Rechnerarchitektur
1. Prozessorarchitektur
	- Befehlssatzarchitektur
		- RISC (V)
			- https://peterhigginson.co.uk/RISC/ --> drin
			- https://riscv.vercel.app/ --> drin
			- https://github.com/riscv-software-src/riscv-isa-sim --> drin
			- https://ascslab.org/research/briscv/simulator/simulator.html --> drin
			- https://github.com/cvut/qtrvsim --> drin
			- https://www.qemu.org/docs/master/system/target-riscv.html --> drin
			- https://www.riscvschool.com/risc-v-simulators/ --> Übersicht
			- ...
		- CISC
			- https://github.com/praveen1496/CISC-simulator --> drin
			- https://github.com/nickcapurso/CISC-Simulator-Group-Project-CSCI-6461 --> drin
			- https://www.harrisburgu.edu/courses/cisc-614/ --> nur für Studis dieser Uni
			- https://www.sciencedirect.com/science/article/abs/pii/016560749390013B --> paper
		 - Mikroarchitektur
			 - https://dl.acm.org/doi/10.1145/800158.805062 --> paper
			 - http://www.mikrocodesimulator.de/ --> drin
	- Pipeline
		- https://vhosts.eecs.umich.edu/370simulators/pipeline/simulator.html --> drin
		- https://wwwpub.zih.tu-dresden.de/~ss17/studium/winter/infet1/docs/mips64/mips_pipe.html --> kein simulator
		- https://github.com/leondavi/simpipe --> drin
	- Superskalarität
		- https://github.com/SSutherlandDeeBristol/superscalar-processor-simulator --> drin
		- https://sc-nas.fit.vutbr.cz:11443/ --> drin
		- https://arxiv.org/abs/2411.07721 --> paper
		- https://github.com/Charana123/Superscalar-CPU-Simulator --> drin
		- https://sc24.supercomputing.org/proceedings/poster/poster_files/post150s2-file3.pdf --> paper
		- https://conferences.computer.org/sc-wpub/pdfs/SC-W2024-6oZmigAQfgJ1GhPL0yE3pS/555400b676/555400b676.pdf --> paper
		- https://sesc.sourceforge.net/ --> drin
	- Registerumbenennung
		- ggf. TOMASULO????
	- Parallelität innerhalb der CPU
		- VLIW
			- https://ieeexplore.ieee.org/document/871022 --> paper
			- https://www.vodafone-chair.org/pbls/legacy/p-schwann/TVLIW++_Instruktionssatzsimulator_fuer_VLIW-DSPs.pdf --> paper
			- https://dl.acm.org/doi/10.1145/1275633.1275636 --> paper
			- https://github.com/divjot0/VLIW-Architecture-Simulation
			- https://ieeexplore.ieee.org/document/4675563 --> paper
			- https://www.sciencedirect.com/science/article/abs/pii/S1569190X16301010 --> paper
			- https://research.ibm.com/publications/vliwsim-an-interactive-simulator-for-vliw-architectures --> paper
 			- https://www.researchgate.net/publication/224349450_Simple-VLIW_A_fundamental_VLIW_architectural_simulation_platform --> paper
		- SIMD
			- https://github.com/TracyGJG/sim-simd
		- MIMD
			- https://www.sciencedirect.com/science/article/abs/pii/S0167819184901819 --> paper
			- https://dl.acm.org/doi/abs/10.5555/2902381.2902643 --> paper
			- https://ieeexplore.ieee.org/document/521024 --> paper
	 - Rechenwerke
		- Boolsche Algebra
			- https://www.boolean-algebra.com/
			- https://de.symbolab.com/solver/boolean-algebra-calculator
			- https://www.emathhelp.net/calculators/discrete-mathematics/boolean-algebra-calculator/
			- https://booleantt.hazeapps.com/
		- Digitale Logik
			- https://logigator.com/de --> drin
			- https://inf-schule.de/rechner/digitaltechnik/Simulatoren/LogicSim --> drin
			- https://digital-logic-sim.de.softonic.com/ --> drin
		- Schaltungen
			- https://www.dotnetpro.de/update/hardware/elektronische-schaltkreise-im-browser-simulieren-1557515.html --> Blog
		- ALU
			- https://github.com/reds-heig/logisim-evolution --> drin
			- https://www.tinkercad.com/circuits --> drin
			- https://github.com/hneemann/Digital --> drin
			- https://www.edaplayground.com/ --> drin
 		- FPU
			- https://www.h-schmidt.net/FloatConverter/ --> drin
			- https://www.binaryconvert.com/ --> drin
			- https://github.com/mortbopet/Ripes --> drin
		- SIMD-Einheiten bspw. für NEON (ARM) oder SSE (x86)
			- https://github.com/mortbopet/Ripes --> drin
			- https://www.gem5.org/ --> drin
			- https://github.com/Multi2Sim/multi2sim --> drin
2. Speicherarchitektur
	- Speicherhierarchie
		- https://csci.csusb.edu/turner/CacheSimulator/
		- https://people.cs.pitt.edu/~childers/CS449/cache/index.html
		- https://peterhigginson.co.uk/lmc/ --> drin
		- https://www.gem5.org/ --> drin
		- http://pages.cs.wisc.edu/~markhill/DineroIV/ --> drin
	- Caching-Techniken
		- https://people.cs.pitt.edu/~childers/CS449/cache/index.html 
		- https://csci.csusb.edu/turner/CacheSimulator/ 
	- Virtueller Speicher
		- https://www.cs.toronto.edu/~penny/vmSimulator.html --> 404
		- https://cdn.cs50.net/2020/fall/lectures/4/src4/paging/ --> 404
		- https://www.nachos-project.org/ --> drin
		- https://web.stanford.edu/class/cs140/projects/pintos/pintos_1.html --> drin
3. Ein-/Ausgabe
	- https://pages.cs.wisc.edu/~remzi/OSTEP/
	- https://github.com/remzi-arpacidusseau/ostep-projects
	- https://people.cs.pitt.edu/~childers/CS449/disk/ --> 404
4. Parallelität und Multiprozessorsysteme
	- https://github.com/mortbopet/Ripes --> drin
	- Little Man Parallel Computer (LMPC) --> drin
	- https://www.gem5.org/ --> drin
	- https://snipersim.org/ --> drin
	- https://github.com/Multi2Sim/multi2sim --> drin
	- https://github.com/gpgpu-sim/gpgpu-sim_distribution --> drin
	- https://github.com/accelsim/accelsim --> 404
5. Energieffizienz und Low-Power-Architekturen
6. Sicherheit und Zuverlässigkeit
7. Spezialprozessoren
8. Betriebsnahe Architektur
9. Forschung
