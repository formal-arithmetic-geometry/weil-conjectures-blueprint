+++
kind = "proof"
of = "sk-lem-pd-generic-restriction"
uses = ["sk-prop-ctf-finite-comparison", "sk-lem-pd-preservation", "sk-cor-pe-bounded-continuity", "sk-def-cd", "sk-thm-purity-transport"]
+++
We prove the comparisons in the order stated, each using the
previous ones: the direct image by continuity along a limit of étale
maps, $i^!$ by the localization triangle, internal Hom by
dévissage to generators $t_!P$, and the twist by a closed embedding
into affine space.

By Proposition [sk-prop-ctf-finite-comparison], with finite coefficients we may
compute $D^b_{\mathrm{ctf}}(X,A)$ and the direct images by their classical
étale counterparts. Recall that a separable closure of
$k(B)$ is the inverse limit of nonempty affine opens in the
normalizations of $B$ in its finite separable extensions, with
the branch loci removed, and that each stage is étale over an open of
$B$. Since each stage is étale over an open of $B$, and pullback to
an étale $B$-scheme is restriction to an object of the small site,
$Rh_*$ commutes with pullback to each stage. Every affine object
étale over the limit descends to a stage, and by continuity of
étale cohomology with finite coefficients along affine transition maps,
the derived sections commute, degree by degree, with this
filtered limit. For this we apply continuity of cohomology
(Corollary [sk-cor-pe-bounded-continuity]), which needs the complexes to
vanish below one fixed degree, and they do because $L$ is bounded. The
base changes of $h$ to the stages are of finite type of bounded
dimension, so their $\ell$-cohomological dimensions
(Definition [sk-def-cd]) are bounded independently of the stage
[Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10), and all the direct images lie in one fixed range of
degrees. Thus the first comparison holds over the separable
closure. Since a purely inseparable extension induces the same classical
étale topos, it also holds over the algebraic closure.

For the second comparison, let $j$ be the open complement of
$i$ and pull back

$$
i_*i^!M\longrightarrow M\longrightarrow Rj_*j^*M
\longrightarrow.
$$

The first comparison identifies the pullback of $Rj_*j^*M$ with
$Rj_{\bar\eta,*}j_{\bar\eta}^*g_X^*M$, and pullback commutes with
direct image along a closed immersion. Hence the pulled-back triangle
is the triangle with closed support on the generic fibre. Since
$i_{\bar\eta,*}$ is fully faithful, the fibres agree, which proves the second
comparison.

For internal Hom, both sides are exact functors of $K$, so the
complexes $K$ for which the comparison is an isomorphism are closed
under cones and shifts. By the dévissage of
Lemma [sk-lem-pd-preservation] it therefore suffices to take $K=t_!P$,
where $t$ is the inclusion of a stratum and $P$ is locally perfect
on it. Then

$$
\cHom_X(t_!P,M)
\simeq Rt_*(P^\vee\otimes^{\mathbf L}t^!M).
$$

Using the first two comparisons, a factorization of $t$ into an open
and a closed immersion, and the dualizability of $P$, we get the claim
for these generators. All complexes
used remain bounded constructible by Lemma [sk-lem-pd-preservation].

Finally, on an affine open of $X$ choose a closed immersion over
$\mathbf A^1_k$ into $\mathbf A^r_{\mathbf A^1_k}$.
Since $\mathbf A^r_{\mathbf A^1_k}$ is smooth of dimension $r+1$ over
$k$, composition and Theorem [sk-thm-purity-transport] give
$\omega_X\simeq i^!A(r+1)[2r+2]$. In the same way, the geometric
generic fibre is a closed subscheme of $\mathbf A^r_{\bar\eta}$, so
$\omega_{X_{\bar\eta}}\simeq i_{\bar\eta}^!A(r)[2r]$. The second
comparison gives
$g_X^*i^!A(r+1)[2r+2]\simeq i_{\bar\eta}^!A(r+1)[2r+2]$, which is
$\omega_{X_{\bar\eta}}(1)[2]$.

It remains to compare the double-dual maps. The comparison for internal
Hom is adjoint to the pullback of the evaluation
$K\otimes^{\mathbf L}\cHom_X(K,M)\to M$, so it carries evaluation to
evaluation. With the twist, it gives
$g_X^*\mathbb D_XK\simeq\mathbb D_{X_{\bar\eta}}(g_X^*K)(1)[2]$ locally
on $X$. Now the double-dual map does not change if the dualizing
complex is replaced by an isomorphic object $\omega'$: an isomorphism
$\omega\simeq\omega'$ enters once in each of the two duals, and the two
occurrences cancel in $\delta$. This applies to
$\omega'=\omega_{X_{\bar\eta}}(1)[2]$, since
$\cHom(\cHom(N,\omega(1)[2]),\omega(1)[2])\simeq\cHom(\cHom(N,\omega),\omega)$
compatibly with evaluation. Hence the isomorphism
$g_X^*\mathbb D_X\mathbb D_XK\simeq\mathbb D_{X_{\bar\eta}} \mathbb D_{X_{\bar\eta}}g_X^*K$ obtained by applying the comparison twice
carries $g_X^*\delta_K$ to $\delta_{g_X^*K}$. Because the local
identification of the twist cancels, this holds on all of $X$.
