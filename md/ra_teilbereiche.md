---
title: "Teilgebiete Rechnerarchitektur"
date: 25.02.2025
tags: "bachelor"
---

# Teilgebiete Rechnerarchitektur
1. Prozessorarchitektur
	- Befehlssatzarchitektur
		- RISC (V)
			- https://peterhigginson.co.uk/RISC/
			- https://riscv.vercel.app/
			- https://github.com/riscv-software-src/riscv-isa-sim
			- https://ascslab.org/research/briscv/simulator/simulator.html
			- https://github.com/cvut/qtrvsim
			- https://www.qemu.org/docs/master/system/target-riscv.html
			- https://www.riscvschool.com/risc-v-simulators/
			- ...
		- CISC
			- https://github.com/praveen1496/CISC-simulator
			- https://github.com/nickcapurso/CISC-Simulator-Group-Project-CSCI-6461
			- https://www.harrisburgu.edu/courses/cisc-614/
			- https://www.sciencedirect.com/science/article/abs/pii/016560749390013B
		 - Mikroarchitektur
			 - https://dl.acm.org/doi/10.1145/800158.805062
			 - http://www.mikrocodesimulator.de/
	- Pipeline
		- https://vhosts.eecs.umich.edu/370simulators/pipeline/simulator.html
		- https://wwwpub.zih.tu-dresden.de/~ss17/studium/winter/infet1/docs/mips64/mips_pipe.html
		- https://github.com/leondavi/simpipe
	- Superskalarität
		- https://github.com/SSutherlandDeeBristol/superscalar-processor-simulator
		- https://sc-nas.fit.vutbr.cz:11443/
		- https://arxiv.org/abs/2411.07721
		- https://github.com/Charana123/Superscalar-CPU-Simulator
		- https://sc24.supercomputing.org/proceedings/poster/poster_files/post150s2-file3.pdf
		- https://conferences.computer.org/sc-wpub/pdfs/SC-W2024-6oZmigAQfgJ1GhPL0yE3pS/555400b676/555400b676.pdf
		- https://sesc.sourceforge.net/
	- Registerumbenennung
		- ggf. TOMASULO????
	- Parallelität innerhalb der CPU
		- VLIW
			- https://ieeexplore.ieee.org/document/871022
			- https://www.vodafone-chair.org/pbls/legacy/p-schwann/TVLIW++_Instruktionssatzsimulator_fuer_VLIW-DSPs.pdf
			- https://dl.acm.org/doi/10.1145/1275633.1275636
			- https://github.com/divjot0/VLIW-Architecture-Simulation
			- https://ieeexplore.ieee.org/document/4675563
			- https://www.sciencedirect.com/science/article/abs/pii/S1569190X16301010
			- https://research.ibm.com/publications/vliwsim-an-interactive-simulator-for-vliw-architectures
			- https://www.researchgate.net/publication/224349450_Simple-VLIW_A_fundamental_VLIW_architectural_simulation_platform
		- SIMD
			- https://github.com/TracyGJG/sim-simd
		- MIMD
			- https://www.sciencedirect.com/science/article/abs/pii/S0167819184901819
			- https://dl.acm.org/doi/abs/10.5555/2902381.2902643
			- https://ieeexplore.ieee.org/document/521024
	 - Rechenwerke
		- Boolsche Algebra
			- https://www.boolean-algebra.com/
			- https://de.symbolab.com/solver/boolean-algebra-calculator
			- https://www.emathhelp.net/calculators/discrete-mathematics/boolean-algebra-calculator/
			- https://booleantt.hazeapps.com/
		- Digitale Logik
			- https://logigator.com/de
			- https://inf-schule.de/rechner/digitaltechnik/Simulatoren/LogicSim
			- https://digital-logic-sim.de.softonic.com/
		- Schaltungen
			- https://www.dotnetpro.de/update/hardware/elektronische-schaltkreise-im-browser-simulieren-1557515.html
		- ALU
			- https://github.com/reds-heig/logisim-evolution
			- https://www.tinkercad.com/circuits
			- https://github.com/hneemann/Digital
			- https://www.edaplayground.com/
 		- FPU
			- https://www.h-schmidt.net/FloatConverter/
			- https://www.binaryconvert.com/
			- https://github.com/mortbopet/Ripes
		- SIMD-Einheiten bspw. für NEON (ARM) oder SSE (x86)
			- https://github.com/mortbopet/Ripes
			- https://www.gem5.org/
			- https://github.com/Multi2Sim/multi2sim
2. Speicherarchitektur
	- Speicherhierarchie
		- https://csci.csusb.edu/turner/CacheSimulator/
		- https://people.cs.pitt.edu/~childers/CS449/cache/index.html
		- https://peterhigginson.co.uk/lmc/
		- https://www.gem5.org/
		- http://pages.cs.wisc.edu/~markhill/DineroIV/
	- Caching-Techniken
		- https://people.cs.pitt.edu/~childers/CS449/cache/index.html
		- https://csci.csusb.edu/turner/CacheSimulator/ 
	- Virtueller Speicher
		- https://www.cs.toronto.edu/~penny/vmSimulator.html
		- https://cdn.cs50.net/2020/fall/lectures/4/src4/paging/
		- https://www.nachos-project.org/
		- https://web.stanford.edu/class/cs140/projects/pintos/pintos_1.html
3. Ein-/Ausgabe
	- https://pages.cs.wisc.edu/~remzi/OSTEP/
	- https://github.com/remzi-arpacidusseau/ostep-projects
	- https://people.cs.pitt.edu/~childers/CS449/disk/
4. Parallelität und Multiprozessorsysteme
	- https://github.com/mortbopet/Ripes
	- Little Man Parallel Computer (LMPC)
	- https://www.gem5.org/
	- https://snipersim.org/
	- https://github.com/Multi2Sim/multi2sim
	- https://github.com/gpgpu-sim/gpgpu-sim_distribution
	- https://github.com/accelsim/accelsim
5. Energieffizienz und Low-Power-Architekturen
6. Sicherheit und Zuverlässigkeit
7. Spezialprozessoren
8. Betriebsnahe Architektur
9. Forschung
