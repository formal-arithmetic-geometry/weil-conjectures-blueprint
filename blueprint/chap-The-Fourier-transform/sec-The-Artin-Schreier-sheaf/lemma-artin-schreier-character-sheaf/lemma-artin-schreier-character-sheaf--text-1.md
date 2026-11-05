+++
id = "lemma-artin-schreier-character-sheaf--text-1"
kind = "hidden"
title = "The Artin–Schreier character sheaf"
order = 1217001
+++
*Shared context for the Lean formulation.* Let $k_0=\Fq$ be a finite field,
let $\ell\ne\operatorname{char}(k_0)$ be prime, and use coefficients
$\Qbarl$. Let $\psi:k_0\to\Qbarl^\times$ be an additive character;
the results below do not require it to be nontrivial. Write
$\mathcal L_{\psi(ax)}$ for the sheaf obtained by pulling the
$\psi$-eigensheaf of $u^q-u=x$ back along $x\mapsto ax$, and put
$\mathcal L_\psi=\mathcal L_{\psi(x)}$. The same family is used throughout.
The two normalization clauses are retained below with an explanation
of their absence from the Lean route.
