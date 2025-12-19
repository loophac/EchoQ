# EchoQ
EchoQ is a minimal, hardware-only quantum experiment designed to probe real-world entanglement behavior and noise on physical quantum computers.

The experiment creates a simple entangled state using a small number of qubits, measures a subset of them, and records the resulting correlations. In an ideal, noise-free system, only perfectly correlated outcomes are expected. On real quantum hardware, additional outcomes appear due to decoherence, gate imperfections, and measurement error.

EchoQ intentionally avoids simulation and noise models.
It is meant to be run only on real quantum hardware, where imperfections are not approximations but physical effects.

EchoQ is designed to be ran with AWS Braket inside a Jupyter notebook for ease of use.
