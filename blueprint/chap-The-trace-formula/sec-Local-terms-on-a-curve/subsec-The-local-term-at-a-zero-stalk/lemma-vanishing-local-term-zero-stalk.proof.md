+++
kind = "proof"
of = "lemma-vanishing-local-term-zero-stalk"
order = 991
uses = ["lemma-flat-models-generators", "definition-pro-etale-base-change-map", "lemma-change-coefficients-compact-support", "lemma-change-coefficients-exceptional-inverse-image", "lemma-external-duality-trace-morphism", "lemma-frobenius-fixed-scheme", "lemma-vanishing-restrictions-after-blowing-up", "lemma-covers-degree-prime-to-ell", "lemma-tangent-cones-on-cover", "lemma-descent-vanishing-finite-etale", "lemma-passing-schematic-closure"]
+++
We use the notation introduced before
Lemma [lemma-covers-degree-prime-to-ell] and compute on the étale
model: we identify $\rho$ with a restriction map $r$ away from $y$, kill
$r$ on a cover with $\ell$-group monodromy, and descend.

*Step 1: reduction to $r$.* Let $N=(\mathbb D_XK)|_{X_1-y}$, the dual
of $K|_{X_1-y}$ with respect to the restriction of $\omega_X$, and let
$Q=K|_{X_2-y}$. Write $j_1:X_1-y\hookrightarrow X_1$ and
$j_2:X_2-y\hookrightarrow X_2$ for the inclusions. As $K_{\bar y}=0$,
localization gives $K|_{X_2}=j_{2!}Q$, and $(\mathbb D_XK)|_{X_1}=Rj_{1*}N$
because the dual of an extension by zero is the direct image of the dual.
The ordinary external Künneth comparison therefore
identifies $P=(\mathbb D_XK\boxtimes K)|_T$ with $Rj_*j'_!(N\boxtimes Q)$,
where

$$
j:T-V\hookrightarrow T,\qquad
j':T-(H\cup V)\hookrightarrow T-V.
$$

Both $R\Gamma(T,P)$ and $R\Gamma(\Delta,\delta^*P)$ are zero, because the
schemes are strictly local and the stalk at the closed point is
$(\mathbb D_XK)_{\bar y}\otimes^{\mathbf L} K_{\bar y}=0$. So the
localization triangles identify $\rho$, shifted by one, with the ordinary
restriction $R\Gamma(T-\Gamma,P)\to R\Gamma(\Delta-y,\delta^*P)$, which
under the Künneth identification is

$$
r:R\Gamma(T-(V\cup\Gamma),j'_!(N\boxtimes Q))
\longrightarrow R\Gamma(\Delta-y,(N\boxtimes Q)|_{\Delta-y}).
$$

*Step 2: the restriction vanishes on a cover.* Choose bounded finite
projective lisse models of $N$ and $Q$ by
Lemma [lemma-flat-models-generators]; their terms are finite locally
constant, as a punctured strictly local trait is its generic point.
Then Lemma [lemma-covers-degree-prime-to-ell], applied to the terms of the
model of $N$ on $X_1-y$ and to those of $Q$ on $X_2-y$, gives integers
$d_1,d_2$ prime to $\ell$. With $d=\operatorname{lcm}(d_1,d_2)$ we then obtain covers $X_1'\to X_1$ and $X_2'\to X_2$ of the same degree $d$. We want equal
degrees so that $u$ and $v$ become $d$th powers for the same $d$ in
Lemma [lemma-tangent-cones-on-cover]. Let $T'$, $\Gamma'$, $V'$,
$\Delta'$, $H'$ be as in that lemma, and let $N'$ and $Q'$ be the pullbacks
of $N$ and $Q$ to $X_1'-y_1'$ and $X_2'-y_2'$. By construction, the complex $N'\boxtimes Q'$ has finite $\ell$-group monodromy on $T'-(H'\cup V')$, hence also on the
smaller open set obtained by removing $\Gamma'$. Then the restriction $r'$ on $T'$, defined like $r$, is zero by
Lemma [lemma-vanishing-restrictions-after-blowing-up], applied to $T'$
with $D=(\Gamma'\cup V')_{\mathrm{red}}$, the regular curve
$H'_{\mathrm{red}}$ and $C=\Delta'_{\mathrm{red}}$; its hypotheses hold by
Lemma [lemma-tangent-cones-on-cover], and passing to reductions changes
neither the open complements nor the étale cohomology.

*Step 3: descent.* The map $r$ followed by pullback to $\Delta'-y'$
equals pullback to $T'$ followed by $r'=0$, because pullback along
$T'\to T$ commutes with restriction and with extension by zero. As $\Delta$
meets $H\cup V$ only at $y$, Lemma [lemma-tangent-cones-on-cover] shows
that $\Delta'-y'\to\Delta-y$ is finite étale of degree $d^2$. This degree is
invertible in $A$, so Lemma [lemma-descent-vanishing-finite-etale] gives
$r=0$, and hence $\rho=0$. By the comparison theorems, this identity on the
classical étale models of these strictly local schemes also holds in the
pro-étale formulation.
Finally, by Lemma [lemma-local-term-restriction-map],
$\operatorname{LT}_y(\psi)$ is the image of $[\psi]$ under a composite that
begins with $\rho$, so it is zero.
