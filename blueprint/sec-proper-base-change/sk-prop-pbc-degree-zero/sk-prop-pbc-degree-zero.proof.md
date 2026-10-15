+++
kind = "proof"
of = "sk-prop-pbc-degree-zero"
uses = ["sk-thm-pbc-henselian-h0"]
+++
Let $Y_{(\bar y)}=\operatorname{Spec}\cO^{\mathrm{sh}}_{Y,\bar y}$ and
$X_{(\bar y)}=X\times_YY_{(\bar y)}$. The degree-zero strict-local stalk
formula gives

$$
(f_*F)_{\bar y}\simeq\Gamma(X_{(\bar y)},F|_{X_{(\bar y)}}).
$$

It holds for quasi-compact quasi-separated $f$ by étale continuity (Stacks
Project, Tag 03Q9; the degree-zero continuity proof there also applies to
sheaves of sets). Recall the mechanism: the left side is the filtered colimit
of $\Gamma(X\times_YV,F|)$ over pointed affine étale neighbourhoods $V$ of
$\bar y$. Their inverse limit is $Y_{(\bar y)}$. A section on the limit is
represented on a finite étale covering of a quasi-compact scheme; the
covering objects, section representatives, and their finitely many agreement
conditions descend to one neighbourhood. This gives surjectivity of the
continuity map; descending the finite agreement conditions for two
representatives gives injectivity.

The local ring of $Y_{(\bar y)}$ is strictly henselian. Its residue field
$\kappa(y)^{\mathrm{sep}}\subseteq\Omega$ is separably closed.
[sk-thm-pbc-henselian-h0] identifies the last section set with sections over
$X_{\kappa(y)^{\mathrm{sep}}}$. Extending a separably closed ground field
preserves sections of a pulled-back étale sheaf (Stacks Project, Tag 0A3I),
so these sections equal $\Gamma(X_{\bar y},F|_{X_{\bar y}})$; here $F|$
denotes inverse image of the given sheaf, also when $\Omega$ is transcendental
over the residue field. This proves the fibre formula.

Now choose $\bar y':\operatorname{Spec}\Omega\to Y'$ and use its composite
$\bar y=g\bar y'$ as the geometric point of $Y$. Properness is preserved by
base change, so the fibre formula applies to $f'$ as well as $f$. The
cartesian square identifies

$$
X'_{\bar y'}=X\times_Y\operatorname{Spec}\Omega=X_{\bar y}
$$

and identifies the two inverse-image sheaves there. Thus the stalks of both
sides of the desired map are the same section set. A section represented over
$X\times_YV$ maps under underived exchange to its restriction over the
base-changed neighbourhood, and hence to its restriction on this same fibre.
The stalk map is therefore the identity under the displayed identifications.
Geometric stalks detect isomorphisms, proving the assertion.
