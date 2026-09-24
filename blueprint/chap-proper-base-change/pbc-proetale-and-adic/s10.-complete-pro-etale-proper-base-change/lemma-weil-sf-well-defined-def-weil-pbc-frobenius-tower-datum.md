+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-frobenius-tower-datum"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-frobenius-tower-datum"
order = 1889
uses = ["def-weil-pbc-frobenius-tower-datum", "lemma-weil-pbc-derived-exchange-coherence", "prop-weil-pbc-proet-finite-level-transport"]
+++
The displayed Frobenius record has fields

$$
\begin{gathered}
\kappa_g:\Phi_{Y'}Lg^*\xrightarrow{\sim}Lg^*\Phi_Y,
\qquad
\kappa_{g'}:\Phi_{X'}L(g')^*\xrightarrow{\sim}L(g')^*\Phi_X,\\
\beta_{f,n}:\Phi_YRf_*K_n\xrightarrow{\sim}Rf_*\Phi_XK_n,
\qquad
\beta_{f',E_n}:\Phi_{Y'}Rf'_*E_n
\xrightarrow{\sim}Rf'_*\Phi_{X'}E_n,\\
\vartheta_n:\Phi_XK_n\xrightarrow{\sim}K_n.
\end{gathered}
$$

The two sides of the tower relation belong to
$\operatorname{Hom}(\Phi_XK_{n+1},K_n)$, so the relation is a typed field of
the record.

## Proof

Pullback by the inverse of $\operatorname{Fr}_Z$ is a quasi-inverse to
$\Phi_Z=L\operatorname{Fr}_Z^*$; hence $\Phi_Z$ is an exact equivalence.
The two pullback faces in the Frobenius cube give $\kappa_g$ and
$\kappa_{g'}$ with the displayed endpoints. Applied to the two proper
faces, finite-level pro-etale transport gives the displayed exchange
isomorphisms because $K_n$ and $E_n$ carry their etale-origin witnesses.
The identity and pasting equations required of these exchanges are those of
Lemma [lemma-weil-pbc-derived-exchange-coherence].

Finally, $\Phi_X(r_{n+1,n})$ has source $\Phi_XK_{n+1}$ and target
$\Phi_XK_n$. Thus
$r_{n+1,n}\vartheta_{n+1}$ and
$\vartheta_n\Phi_X(r_{n+1,n})$ have the common source and target stated in
the lemma. This verifies the record typing without asserting a new
Frobenius-equivariance theorem for the finite rectangle.
