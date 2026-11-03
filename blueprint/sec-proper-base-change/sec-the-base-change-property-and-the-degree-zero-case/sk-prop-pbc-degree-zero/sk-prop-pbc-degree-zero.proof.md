+++
kind = "proof"
of = "sk-prop-pbc-degree-zero"
uses = ["sk-thm-pbc-henselian-h0"]
+++
We show that both stalks are the sections over the same geometric fibre.
Let $y\in Y$ be the image of $\bar y$, let
$Y_{(\bar y)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y,\bar y}$
and $X_{(\bar y)}=X\times_YY_{(\bar y)}$. In degree zero the stalk is
computed on the strict localization, that is,

$$
(f_*F)_{\bar y}\simeq\Gamma(X_{(\bar y)},F|_{X_{(\bar y)}}).
$$

For quasi-compact quasi-separated $f$ this holds by continuity of étale
sections ([Stacks, Tag 03Q9](https://stacks.math.columbia.edu/tag/03Q9), whose proof in degree zero applies to sheaves
of sets). Indeed, the stalk $(f_*F)_{\bar y}$ is the filtered colimit of
$\Gamma(X\times_YV,F|)$ over pointed affine étale neighbourhoods $V$
of $\bar y$, where $F|$ denotes the inverse image of $F$, and the limit
of these neighbourhoods is $Y_{(\bar y)}$. A section over the limit,
together with the finitely many covering objects and agreement
conditions that represent it, descends to one neighbourhood. This proves
surjectivity, and the same descent for two representatives proves
injectivity.

The local ring of $Y_{(\bar y)}$ is strictly henselian, with separably
closed residue field $\kappa(y)^{\mathrm{sep}}\subseteq\Omega$.
By Theorem [sk-thm-pbc-henselian-h0] the set of sections on the right is
identified with the set of sections over $X_{\kappa(y)^{\mathrm{sep}}}$.
Extending a separably closed ground field does not change the sections of
the pullback of an étale sheaf [Stacks, Tag 0A3I](https://stacks.math.columbia.edu/tag/0A3I), so these sections equal
$\Gamma(X_{\bar y},F|_{X_{\bar y}})$. This proves (4.5).

Now choose $\bar y':\operatorname{Spec}\Omega\to Y'$ and use the
composite $\bar y=g\bar y'$ as the geometric point of $Y$. Properness
is preserved by base change, so (4.5) applies to $f'$ as
well as to $f$. The cartesian square identifies

$$
X'_{\bar y'}=X\times_Y\operatorname{Spec}\Omega=X_{\bar y}
$$

and identifies the two inverse image sheaves on it. Thus the stalks of
both sides of the desired map are the same set of sections. The underived
base change map sends a section
represented over $X\times_YV$ to its
restriction to the base change of the neighbourhood, and hence to its
restriction to this same fibre. In other words, the map on stalks is the
identity under the displayed identifications. Since geometric stalks detect
isomorphisms, this proves the assertion.
