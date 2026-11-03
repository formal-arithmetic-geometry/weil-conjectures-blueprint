+++
kind = "proof"
of = "det-ctf-finite-proper-tor"
+++
*Constructibility.* $Rp_*C\in\Dbc(Y_{\mathrm{ét}},A)$ by [lem-fin-proper-bounded-constructible].

*Stalks of tensor products.* Let $N$ be an $A$-module and $\bar y$ a geometric point of $Y$. The projection
formula for a constant module ([Stacks, Tag 0F12](https://stacks.math.columbia.edu/tag/0F12)) gives $(Rp_*C)\otimes^{\mathbf L}_AN_Y\simeq Rp_*(C\otimes^{\mathbf L}_AN_X)$,
and proper base change ([sk-thm-properbasechange]) identifies its stalk at $\bar y$ with

$$
R\Gamma\bigl(X_{\bar y},C|_{X_{\bar y}}\otimes^{\mathbf L}_AN_{X_{\bar y}}\bigr).
$$

The complex $C\otimes^{\mathbf L}_AN$ has cohomology sheaves in $[a,b]$ by the Tor amplitude hypothesis, and
$H^p(X_{\bar y},-)$ vanishes on torsion sheaves for $p>d$; the hypercohomology spectral sequence gives
cohomology in $[a,b+d]$.

*From constant modules to all sheaves.* Tor amplitude in $[a,b+d]$ means that
$Rp_*C\otimes^{\mathbf L}_AM$ has cohomology in $[a,b+d]$ for every sheaf of $A$-modules $M$; this can be tested on
stalks, and $(Rp_*C\otimes^{\mathbf L}_AM)_{\bar y}=(Rp_*C)_{\bar y}\otimes^{\mathbf L}_AM_{\bar y}$ (a flat resolution of
$Rp_*C$ restricts at every geometric point to a flat resolution of the stalk, and tensor products are
computed stalkwise). Taking $N=M_{\bar y}$ above, $(Rp_*C)_{\bar y}\otimes^{\mathbf L}_AN=(Rp_*C\otimes^{\mathbf L}_AN_Y)_{\bar y}$
has cohomology in $[a,b+d]$. Hence $Rp_*C$ has Tor amplitude in $[a,b+d]$.
