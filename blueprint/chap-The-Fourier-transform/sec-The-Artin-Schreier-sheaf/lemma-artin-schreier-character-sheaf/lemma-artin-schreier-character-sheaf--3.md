+++
id = "lemma-artin-schreier-character-sheaf--3"
kind = "lemma"
title = "Dual character"
order = 1220006
aliases = ["bp-r375-3"]
lean = ["AlgebraicGeometry.nonempty_iso_dual_artinSchreier"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1", "definition-change-of-coefficients-maps--6", "proposition-six-operations-change-coefficients--23", "proposition-sp-unique-adjoint--1", "definition-weil-structure--1", "definition-weil-structure--3", "definition-compactification-refinement--1"]
+++
For $a\in k_0$ write $\mathcal L_{\psi(ax)}=\mathcal L_{\psi,ax}$ for the
pullback of $\mathcal L_\psi$ along $x\mapsto ax$, in the notation of
[lemma-artin-schreier-character-sheaf--2], and define
$\mathcal L_{\psi^{-1}(ax)}$ in the same way from the sheaf
$\mathcal L_{\psi^{-1}}$ of the nontrivial character $\psi^{-1}$. For every
$a\in k_0$ there is an isomorphism of Weil sheaves

$$
\mathcal L_{\psi(ax)}^\vee\simeq\mathcal L_{\psi^{-1}(ax)}.
$$

Here the dual is the internal hom into the constant Weil sheaf.
The case $a=1$ gives $\mathcal L_\psi^\vee\simeq\mathcal L_{\psi^{-1}}$.
No compatibility with a chosen trivialization at zero is asserted.
