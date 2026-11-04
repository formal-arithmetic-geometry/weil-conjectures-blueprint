+++
kind = "proof"
of = "lemma-sections-geometric-fibre"
order = 332
uses = ["theorem-comparison-over-henselian-pair-degree"]
+++
Let $y\in Y$ be the image of $\bar y$, let
$Y_{(\bar y)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y,\bar y}$
and $X_{(\bar y)}=X\times_YY_{(\bar y)}$. In degree zero the stalk is
computed on the strict localization, that is,

$$
(f_*F)_{\bar y}\simeq\Gamma(X_{(\bar y)},F|_{X_{(\bar y)}}).
$$

For quasi-compact quasi-separated $f$ this holds by continuity of étale
sections ([Stacks, [03Q9](https://stacks.math.columbia.edu/tag/03Q9)], whose proof in degree zero applies to sheaves
of sets). By definition, the stalk $(f_*F)_{\bar y}$ is the filtered colimit of
$\Gamma(X\times_YV,F|)$ over pointed affine étale neighbourhoods $V$
of $\bar y$, where $F|$ denotes the inverse image of $F$. Since the limit
of these neighbourhoods is $Y_{(\bar y)}$, there is a natural map from
the colimit to the sections over $X_{(\bar y)}$. We must see that it is
bijective. A section over the limit is represented by finitely many
covering objects and finitely many agreement conditions, because
$X_{(\bar y)}$ is quasi-compact and quasi-separated. All these data are of
finite presentation, so they descend to one neighbourhood. This proves
surjectivity, and the same descent for two representatives proves
injectivity.

The local ring of $Y_{(\bar y)}$ is strictly henselian, with separably
closed residue field $\kappa(y)^{\mathrm{sep}}\subseteq\Omega$. Thus
$\mathcal O^{\mathrm{sh}}_{Y,\bar y}$ with its maximal ideal is a henselian
pair, and $X_{(\bar y)}$ is proper over it with closed fibre
$X_{\kappa(y)^{\mathrm{sep}}}$. Theorem [theorem-comparison-over-henselian-pair-degree] therefore identifies the
sections on the right with those
over $X_{\kappa(y)^{\mathrm{sep}}}$. These in turn equal
$\Gamma(X_{\bar y},F|_{X_{\bar y}})$, because extending a separably closed
ground field from $\kappa(y)^{\mathrm{sep}}$ to $\Omega$ does not change
the sections of the pullback of an étale sheaf [Stacks, [0A3I](https://stacks.math.columbia.edu/tag/0A3I)].
