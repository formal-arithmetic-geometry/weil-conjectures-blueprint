+++
kind = "proof"
of = "det-sf-comp-coherence-cocycle"
uses = ["det-sf-comp-coherence-refinement", "sk-lem-nagata-density-normalization", "sk-prop-nagata-sketch-comp-category"]
+++
*Dense replacement.* Replacing $Z_a$ by the scheme-theoretic closure
$\overline{j_a(X)}$ does not change $Rp_{a*}j_{a!}$
([sk-lem-nagata-density-normalization]): the closed immersion
$\iota:\overline{j_a(X)}\to Z_a$ is itself a refinement, and $e_\iota$ is an
isomorphism by [det-sf-comp-coherence-refinement]. Composing with these
isomorphisms we may assume all compactifications dense.

*Refinement isomorphisms.* For a refinement $h:Z'\to Z$ over $Y$ between
dense compactifications put
$\rho_h=Rp_*(e_h):Rp_*j_!\xrightarrow{\sim}Rp_*Rh_*j'_!=R(ph)_*j'_!$, an
isomorphism $Rf_!^{c}\to Rf_!^{c'}$ by [det-sf-comp-coherence-refinement] (2).
By (3) of that lemma, $\rho_{\mathrm{id}}=\mathrm{id}$ and
$\rho_{hk}=\rho_k\circ\rho_h$ for successive refinements.

*Definition.* Given $c_1,c_2$, choose a common dense refinement $c$ with
$h_a:Z\to Z_a$, $h_a^{-1}(X)=X$ ([sk-prop-nagata-sketch-comp-category]) and put
$\phi_{c_2,c_1}=\rho_{h_2}^{-1}\circ\rho_{h_1}$.

*Independence.* Let $c'$ with $h'_a:Z'\to Z_a$ be another common dense
refinement. Choose a common dense refinement $c''$ of $c$ and $c'$, with
$k:Z''\to Z$ and $k':Z''\to Z'$. The composites $h_a\circ k$ and $h'_a\circ k'$
are both refinements $Z''\to Z_a$; they restrict to the identity on the dense
open $X$ and $Z_a$ is separated over $Y$, so they are equal. By
transitivity, $\rho_{h_ak}=\rho_k\rho_{h_a}$ and
$\rho_{h'_ak'}=\rho_{k'}\rho_{h'_a}$, and therefore

$$
\rho_{h_2}^{-1}\rho_{h_1}=\rho_{h_2}^{-1}\rho_k^{-1}\rho_k\rho_{h_1}
=\rho_{h_2k}^{-1}\rho_{h_1k}
=\rho_{h'_2k'}^{-1}\rho_{h'_1k'}
=\rho_{h'_2}^{-1}\rho_{h'_1}.
$$

*Cocycle.* For three compactifications choose one common dense refinement
$c$ of all three, with maps $h_1,h_2,h_3$. Then, by independence,
$\phi_{c_3,c_2}\phi_{c_2,c_1}=\rho_{h_3}^{-1}\rho_{h_2}\rho_{h_2}^{-1}\rho_{h_1}
=\rho_{h_3}^{-1}\rho_{h_1}=\phi_{c_3,c_1}$, and $\phi_{c,c}=\mathrm{id}$ by taking
$c$ itself as common refinement.
