+++
kind = "proof"
of = "det-pd-dual-stratum-extension"
uses = ["cor-pur-dualizing-object-purity", "det-pd-dualizing-complex-ctf", "det-sf-flat-model-generation", "det-thm-sf-ctf-stability-direct-images", "lem-pod-coefficient-dual-perfect", "lem-sf-tensor-hom"]
+++
**(1)** The immersion $t$ is separated of finite type and $Rt_!=t_!$. The
internal adjunction [lem-sf-tensor-hom] with $M=P$ and
$N=\omega_X$ gives

$$
\mathbb D_X(t_!P)=\cHom_X(t_!P,\omega_X)\simeq Rt_*\cHom_T(P,t^!\omega_X),
$$

and $t^!\omega_X\simeq\omega_T$ by [det-pd-dualizing-complex-ctf]. This is the
first isomorphism. Since $T$ is smooth of pure dimension $r$ over $k$, smooth
purity [cor-pur-dualizing-object-purity] for $a_T$ and $A_s$ gives
$\omega_T\simeq A_T(r)[2r]$. The twist $A_T(r)$ is invertible, so

$$
\mathbb D_TP=\cHom_T(P,A_T(r)[2r])\simeq P^\vee(r)[2r].
$$

The complex $P$ is perfect over $A_T$, so $P^\vee$ is perfect over $A_T$ and
lies in $\Dctf(T,A)$ [lem-pod-coefficient-dual-perfect]; so does its twist and
shift. The ordinary direct image $Rt_*$ preserves $\Dctf$
[det-thm-sf-ctf-stability-direct-images], so
$\mathbb D_X(t_!P)\in\Dctf(X,A)$.

**(2)** Take a bounded complex of flat constructible sheaves representing $K$,
and a finite stratification on which every term is locally constant with
finite projective stalks [det-sf-flat-model-generation]. The base field $k$ is
finite or algebraically closed, hence perfect, so after passing to the reduced
subschemes, which does not change the site, the strata may be refined to be
smooth of pure dimension. On a stratum $T$ the restriction $P=K|_T$ is then a
bounded complex of locally constant sheaves with finite projective stalks,
that is, a locally constant perfect complex. The open–closed localization
triangles along the stratification, or the stupid filtration of the flat
model, build $K$ from the $t_!P$ by finitely many shifts and cones. The functor
$\mathbb D_X$ is exact, and $\Dctf(X,A)$ is closed under shifts and cones, so
(1) gives $\mathbb D_XK\in\Dctf(X,A)$.
