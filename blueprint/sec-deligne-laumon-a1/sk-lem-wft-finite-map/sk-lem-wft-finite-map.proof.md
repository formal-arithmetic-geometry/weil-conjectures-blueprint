+++
kind  = "proof"
of    = "sk-lem-wft-finite-map"
+++
Let $\overline C_0$ be the smooth projective completion, choose a
closed point $s$ of $\overline C_0$ outside $C_0$, and put
$d_s=[\kappa(s):k_0]$. Choose $m$ prime to $p$ with
$(m-1)d_s>2g(\overline C_0)-2$. By Riemann–Roch ([sk-thm-picard-rr]),

$$
 h^0(\mathcal O(ms))-h^0(\mathcal O((m-1)s))=d_s>0.
$$

Hence there is a function $f$ whose only pole is at $s$, of exact
order $m$. The sections $1,f$ define a nonconstant map
$\overline C_0\to\mathbf P^1$ whose inverse image of infinity
is $\{s\}$. This map is proper with finite fibres, hence finite
([sk-prop-av-pqf-finite]).
To see that it is generically étale, choose a uniformizer $t$ at $s$
and write $f=t^{-m}u$ with $u$ a unit. Since $\kappa(s)/k_0$ is
separable and the curve is smooth, $dt$ generates the module of
differentials near $s$. Writing $du=h\,dt$, we get

$$
 df=t^{-m-1}(-mu+th)\,dt\ne0,
$$

because $p\nmid m$. Thus the differential of this finite map between
smooth curves is invertible at the generic point, and so the map is
generically étale. We set $C'_0=\overline C_0\setminus\{s\}$ and
let $g$ be the restriction of the map to $C'_0$.

Over the open in the statement, $g$ is finite étale and its inverse
image lies in $C_0$, so $K$ is lisse there. At a closed point $y$ of
this open, the stalk of $K$ is a sum over the geometric points of the
fibre, which Frobenius permutes. On a cycle of residue degree $e$, the
$e$th power of the operator is the local Frobenius upstairs. Hence an
eigenvalue $\beta$ satisfies $|\iota\beta|^e=q_y^{ew/2}$, and the
weight is still $w$. Finally, $Rg_!=g_*$ since $g$ is finite, and the
identification of cohomology follows from the composition of
compact-support direct images ([sk-thm-sf-package]). The construction
is defined over $k_0$, so it commutes with Frobenius.
