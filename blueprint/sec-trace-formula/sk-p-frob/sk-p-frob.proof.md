+++
kind = "proof"
of = "sk-p-frob"
uses = ["sk-i-additivity", "sk-i-curve-zero", "sk-p-proper", "sk-p-pairing", "sk-lem-tf-fixed-points", "sk-d-weil"]
+++
Let $i:\{y\}\hookrightarrow X$ and $j:X\setminus\{y\}\hookrightarrow X$.
Both pieces are stable under $\Phi_X^m$; in particular
$((\Phi_X^m)^{-1}\{y\})_{\mathrm{red}}=\{y\}$. In the enhanced derived
category the functorial open–closed triangle is a two-step filtered
object,

$$
 K_U=j_!j^*K\longrightarrow K\longrightarrow K_y=i_*i^*K
 \xrightarrow{+1}.
$$

The map $v$ induces a coherent map from the $(\Phi_X^m)^*$-pullback of this
filtration to the filtration itself, by two base-change identities.
Inverse-image base change for the Cartesian open square gives
$(\Phi_X^m)^*j_!\simeq j_!(\Phi_X^m|_U)^*$, where $U=X\setminus\{y\}$. The square for the
point is Cartesian only after passing to reductions, so proper base change followed by
nilpotent invariance gives $(\Phi_X^m)^*i_*\simeq i_*(\Phi_X^m|_y)^*$. Both comparisons are
mates of the open–closed adjunction units used in the triangle, and the two
graded correspondences are $v_U$ and $i_*v_{\bar y}$.

Filtered trace-class additivity
([sk-i-additivity]) gives

$$
 \operatorname{LT}_y(v)
 =\operatorname{LT}_y(v_U)
  +\operatorname{LT}_y(i_*v_{\bar y}).
$$

The first term is zero by
[sk-i-curve-zero], since
$(K_U)_{\bar y}=0$. By the description of the closed graded correspondence in
[sk-i-additivity], the second term is the
proper pushforward of the identity correspondence on the point. The
proper pushforward compatibility of
[sk-p-proper], followed by
[sk-p-pairing], identifies it
with $\operatorname{tr}_A(v_{\bar y}\mid K_{\bar y})$, the trace of
the perfect complex $K_{\bar y}$.

*Complement.* As in the complement of [sk-i-curve-zero], $X_0$ is a smooth curve, $\varphi_m$
is a morphism $\Phi_m^*K\to K$ with $\Phi_m=\Phi_X^m$, and by [sk-lem-tf-fixed-points] the
clopen subscheme $B$ is the reduced point component $\{\bar x\}$ of $\Fix(1,\Phi_m)$, so
$\LT_B(\varphi_m)=\LT_{\bar x}(\varphi_m)$. The assertion is the case $v=\varphi_m$,
$y=\bar x$ of the proposition, since $F_{x,m}=(\varphi_m)_{\bar x}$ by [sk-d-weil].
