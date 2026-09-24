+++
id = "lemma-weil-efi-site-adjunction-hom-backward-descent"
kind = "lemma"
title = "Descent of the reverse Hom formula"
order = 1776
uses = ["def-weil-efi-site-adjunction-hom-backward-presheaf", "def-weil-pbc-epsilon-factorization-index-v1"]
+++
The representative formula factors uniquely through pro-etale
sheafification.

## Proof

For a transition $h:U'\to U$ with $a=\iota_X(h)a'$, naturality of $\beta$
and functoriality of $G$ identify the values of $(a,s)$ and
$(a',F(h)s)$. Restriction along $b:W'\to W$ changes each formula to
$G(ab)(\beta_U(s))$. Local equality descends because $G$ is a sheaf. The
universal property of sheafification gives the unique factorization.
