+++
kind = "proof"
of = "lemma-local-duality-point-c-u--1"
order = 1291002
uses = ["proposition-extension-zero-restriction-closed-subscheme", "lemma-local-cohomology-right-adjoint", "proposition-six-operations-dctf", "theorem-verdier-biduality", "corollary-verdier-exchange-formulas", "corollary-dualizing-complex-smooth-scheme"]
+++
Take the reduced closed complement $i_0:Z_0\hookrightarrow C_0$.
It is finite over $k_0$: the complement of a dense open in a noetherian
curve has finitely many points, all closed. Let $i:Z\hookrightarrow C$
be its base change and put $A(F)=i^*Rj_*F$.

The adjunctions of [proposition-six-operations-dctf] and
[lemma-local-cohomology-right-adjoint] give $i^!Rj_*G=0$.
Apply $i^!$ to the localization triangle of
[proposition-extension-zero-restriction-closed-subscheme] for $Rj_*G$.
Using $j^*Rj_*G\simeq G$ and $i^!i_*\simeq\operatorname{id}$ gives
$i^!j_!G\simeq(i^*Rj_*G)[-1]$. Verdier exchange and biduality
([corollary-verdier-exchange-formulas], [theorem-verdier-biduality])
therefore give an isomorphism

$$
\mathbb D_Z A(F)\simeq(i^*Rj_*\mathbb D_UF)[-1].
$$

Since $F$ is lisse, internal Hom out of $F$ is tensor product with
$F^\vee$. The smooth dualizing complex of
[corollary-dualizing-complex-smooth-scheme] identifies
$\mathbb D_UF$ with $F^\vee(1)[2]$. Thus

$$
\mathbb D_Z A(F)\simeq A(F^\vee(1))[1].
$$

The finite reduced scheme $Z_0$ is étale over $k_0$. Its dualizing
complex is the constant sheaf in degree zero, and duality on its Weil
sheaves is exact. Taking degree $-1$, using exactness of $i^*$ and
$\mathcal H^0(Rj_*)=j_*$, gives

$$
(\mathcal H^1 A(F))^\vee\simeq i^*((j_*F^\vee)(1)).
$$

Here the degree $-1$ comparison is obtained by dualizing the two
truncation triangles that isolate $\mathcal H^1A(F)$; this is
`AlgebraicGeometry.WeilComplex.nonempty_homologySheaf_neg_one_verdierDual_iso`.
Taking stalks at the point of $Z_0$ over $s$ commutes with the closed
pullback, the dual, and the twist. These comparisons respect Frobenius,
and the twist $(1)$ multiplies local Frobenius by $q_s^{-1}$.
They give a Frobenius-equivariant isomorphism $V(1)\simeq W^\vee$.
After forgetting the twist on the underlying vector space, its
equivariance is precisely
$e(\operatorname{Frob}_s a)(\operatorname{Frob}_s b)=q_s e(a)(b)$.
