+++
kind = "proof"
of = "thm-lisse-qlbar-representations"
uses = ["cor-galois-lisse-representations", "thm-galois-fundamental", "sk-prop-pe-condensed-point", "sk-prop-pe-finite-local-systems", "sk-prop-sfb-qlbar-colimit-x", "sk-lem-stratified-lattice", "det-lem-stratified-lattice-rank", "det-lem-stratified-lattice-scheme", "det-lem-coefficient-finite-descent-lisse", "det-lem-coefficient-finite-descent-sections"]
+++
Write $A_n=\mathcal O_E/\pi_E^n$. A lisse module on the connected $X$ has
constant rank $r$ ([det-lem-stratified-lattice-rank]).

*Fibres.* Pro-étale sheaves on $\Spec\kappa$ are sheaves on profinite sets,
and every cover of the point has a section
([sk-prop-pe-condensed-point]). So a lisse $\Lambda$-module on $\Spec\kappa$
is free, $\Gamma(\Spec\kappa,-)$ is exact on it, and
$\Lambda_{\Spec\kappa}(\Spec\kappa)=\Lambda$. Inverse image $\bar x^*$ is
exact and commutes with $\otimes$ and with $\nu^*$; for a classical sheaf
$\nu^*\mathcal F$ the fibre is the étale stalk $\mathcal F_{\bar x}$.

*(1) Integral coefficients.* Let $L_0$ be a lisse $\mathcal O_{E,X}$-module
of rank $r$ and $L_n=L_0/\pi_E^nL_0$. Locally $L_n\cong A_{n}^{\oplus r}$, so
$L_n=\nu^*\mathcal L_n$ for a locally constant sheaf $\mathcal L_n$ of finite
free $A_n$-modules on $X_{\mathrm{\acute et}}$, and $\nu^*$ is fully faithful
on such sheaves ([sk-prop-pe-finite-local-systems]). By
[cor-galois-lisse-representations], $M_n=\mathcal L_{n,\bar x}$ is a finite
free $A_n$-module with a continuous $\pi_1$-action, and the transition
isomorphisms $L_{n+1}\otimes A_n\cong L_n$ give equivariant isomorphisms
$M_{n+1}\otimes A_n\cong M_n$. By [sk-prop-sfb-qlbar-colimit-x],
$\mathcal O_{E,X}\cong\varprojlim_n(A_n)_X$; since $L_0$ is locally free of
finite rank, $L_0\cong\varprojlim_nL_n$. On $\Spec\kappa$, $\bar x^*L_0$ is
free of rank $r$, and $\Gamma$ commutes with limits, so
$L_{0,\bar x}=\varprojlim_nM_n$, a free $\mathcal O_E$-module of rank $r$.
The action of $\pi_1$ on it is continuous for the $\pi_E$-adic topology,
because the action on each $M_n$ factors through a finite quotient.

Full faithfulness. For lisse $L_0,L'_0$,
$$
\Hom(L_0,L'_0)=\varprojlim_n\Hom(L_0,L'_n)=\varprojlim_n\Hom_{A_n}(L_n,L'_n)
=\varprojlim_n\Hom_{\pi_1}(M_n,M'_n)=\Hom_{\pi_1}(M,M'),
$$
using $L'_0=\varprojlim L'_n$, that $L'_n$ is killed by $\pi_E^n$, full
faithfulness of $\nu^*$ and [cor-galois-lisse-representations]; the last
equality holds because an $\mathcal O_E$-linear map
$M\to M'=\varprojlim M'_n$ is a compatible family of maps
$M_n\to M'_n$, and it is equivariant if and only if each of them is.

Essential surjectivity. Let $\pi_1$ act continuously on $M\cong\mathcal
O_E^{\oplus r}$, and put $M_n=M/\pi_E^nM$. Each $M_n$ is finite with a
continuous action, so by [cor-galois-lisse-representations] it is the fibre of
a locally constant $\mathcal L_n$, compatibly in $n$. Let $G_n$ be the
finite image of $\pi_1$ in $\operatorname{Aut}(M_n)$ and $Y_n\to X$ the
corresponding connected finite étale Galois cover
([thm-galois-fundamental]), with compatible maps $Y_{n+1}\to Y_n$ and points
over $\bar x$. Then $\mathcal L_n|_{Y_n}$ is constant with value $M_n$,
compatibly in $n$. The limit $Y=\varprojlim Y_n$ is affine over $X$ and
surjective, so it is a pro-étale cover of $X$, and on $Y$ all $L_n=\nu^*\mathcal
L_n$ are constant, compatibly. Put $L_0=\varprojlim_nL_n$. Restriction to $Y$
commutes with limits, so by [sk-prop-sfb-qlbar-colimit-x]
$$
L_0|_Y\cong\varprojlim_n(M_n)_Y\cong\varprojlim_n(A_n)_Y^{\oplus r}
\cong\mathcal O_{E,Y}^{\oplus r}.
$$
Hence $L_0$ is lisse, the map $L_0/\pi_E^n\to L_n$ is an isomorphism, being one
on $Y$, and $L_{0,\bar x}\cong M$ equivariantly. The compatibility with
reduction modulo $\pi_E^n$ holds by construction.

*(2) Rational coefficients.* Let $L$ be integral with lattice $L_0$ and put
$V=L_{\bar x}=L_{0,\bar x}[1/\ell]$, since $\bar x^*$ and $\Gamma$ on the point
commute with $[1/\ell]$. Morphisms. Since $L_0$ is locally free of finite
rank, $\mathcal Hom(L_0,-)$ commutes with filtered colimits, and global
sections on the qcqs $X$ commute with filtered colimits
([det-lem-coefficient-finite-descent-sections] (1)). For integral $L,L'$ with
lattices $L_0,L'_0$, $L'$ is the colimit of $\pi_E^{-c}L'_0$, so
$$
\Hom_{E_X}(L,L')=\Hom(L_0,L')=\varinjlim_c\Hom(L_0,\pi_E^{-c}L'_0)
=\varinjlim_c\Hom_{\pi_1}(M,\pi_E^{-c}M')=\Hom_{\pi_1}(V,V')
$$
by (1); the last equality holds because $M$ is finitely generated, so an
equivariant $V\to V'$ maps $M$ into some $\pi_E^{-c}M'$. Independence of the
lattice. If $L_0,L'_0$ are two lattices in $L$, then on a finite trivializing
cover each is a locally constant function to the discrete set of lattices in
$E^r$, with finitely many values ([det-lem-stratified-lattice-scheme] (1)),
so $\pi_E^cL_0\subseteq L'_0$ for some $c$. By (1) this inclusion induces an
equivariant map $L_{0,\bar x}\to L'_{0,\bar x}$, which becomes $\pi_E^c$
times the identity of $V$ after inverting $\ell$; so the two actions on $V$
agree. Essential surjectivity. Let $\pi_1$ act continuously on a
finite-dimensional $E$-space $V$ and let $M_0\subset V$ be a lattice. Its
stabilizer is open, being the preimage of the open subgroup
$\operatorname{Aut}(M_0)$, hence of finite index in the profinite $\pi_1$,
so $M=\sum_{g\in\pi_1}gM_0$ is a finite sum of lattices, a $\pi_1$-stable
lattice. By (1), $M$ is the fibre of a lisse $L_0$, and $L=L_0[1/\ell]$ has
fibre $V$. Tensor products are compatible because they are so at each finite
level ([cor-galois-lisse-representations]).

*(3) $\Qlb$-coefficients.* Let $L\cong\QbarX\otimes_{E_X}L'$ with $L'$
integral. If $L'$ has lattice $L'_0$, then for finite $F\supseteq E$ the
module $L'_F$ has the lattice $\mathcal O_{F,X}\otimes_{\mathcal O_{E,X}}L'_0$,
and its fibre is $F\otimes_EL'_{\bar x}$ with the extended action, by (1);
so $L_{\bar x}=\Qlb\otimes_EL'_{\bar x}$ is defined over $E$. Two models
$L',L''$ of $L$ become isomorphic over a finite $F$
([det-lem-coefficient-finite-descent-lisse] (2)), and by (2) over $F$ their
fibres are then equivariantly isomorphic, so the action on $L_{\bar x}$ does
not depend on the model. Morphisms. For integral $L',L''$ over $E$, with
fibres $V',V''$,
$$
\Hom_{\QbarX}(L'_{\Qlb},L''_{\Qlb})=\varinjlim_F\Hom_{F_X}(L'_F,L''_F)
=\varinjlim_F\Hom_{\pi_1}(V'_F,V''_F)
$$
by [det-lem-coefficient-finite-descent-lisse] (2) and (2). With
$W=\Hom_E(V',V'')$, the last group is $\varinjlim_FW^{\pi_1}\otimes_EF=
W^{\pi_1}\otimes_E\Qlb$: the invariants of the finite-dimensional $W$ are
the kernel of finitely many maps $w\mapsto gw-w$, which commutes with the flat
extensions $-\otimes_EF$ and $-\otimes_E\Qlb$. Hence it equals
$(W\otimes_E\Qlb)^{\pi_1}=\Hom_{\pi_1}(V'_{\Qlb},V''_{\Qlb})$. Essential
surjectivity. A representation defined over $E$ is $\Qlb\otimes_EV_E$ with
$V_E$ continuous, and (2) gives an integral $L'$ with fibre $V_E$.

*(4) Normality.* A regular $X$ is normal, since its local rings are regular
and a regular ring is normal ([Stacks, Tag 0567](https://stacks.math.columbia.edu/tag/0567)). Let $X$ be normal, and let $L$
be a lisse $E_X$-module of rank $r$. Since $X$ is Noetherian, normal and
connected, it is integral ([Stacks, Tag 033M](https://stacks.math.columbia.edu/tag/033M)); let $\eta$ be its generic point. By [sk-lem-stratified-lattice] there is a finite
stratification of $X$ with a lattice on each stratum. The stratum containing
$\eta$ is locally closed and contains the generic point, so it contains a
dense open $U$, and $L|_U$ has a lattice. Let $q:T=\mathrm{Lat}(L)\to X$ be the
separated étale scheme of lattices of [det-lem-stratified-lattice-scheme];
the lattice on $U$ is a section $s:U\to T_U=T\times_XU$.

The scheme $T$ is étale over the Noetherian normal $X$, so it is locally
Noetherian and normal, an étale ring map being smooth ([Stacks, Tag 033C](https://stacks.math.columbia.edu/tag/033C)). Hence
$T$ is a disjoint union of normal integral schemes ([Stacks, Tag 033N](https://stacks.math.columbia.edu/tag/033N)), and its
connected components are open, closed and irreducible. A section of a
separated étale morphism is an open and closed immersion ([Stacks, Tag 024T](https://stacks.math.columbia.edu/tag/024T)), so
$s(U)$ is open and closed in $T_U$. Let $T'$ be the connected
component of $T$ containing the connected set $s(U)$. The open subset
$T'_U$ of the irreducible $T'$ is irreducible, hence connected, and contains
$s(U)$ as an open and closed subset, so $T'_U=s(U)$ and $q$ restricts to an
isomorphism $T'_U\cong U$.

Let $\bar y$ be a geometric point of $X$ and $X^{\mathrm{sh}}$ the spectrum
of the strict henselization at $\bar y$. Since $X$ is normal, its local
ring at the image of $\bar y$ is a normal domain, so the strict henselization
is a normal domain ([Stacks, Tag 06DI](https://stacks.math.columbia.edu/tag/06DI)): $X^{\mathrm{sh}}=\Spec R$ is irreducible,
and its generic point lies over $\eta\in U$. The étale surjective
$T\times_XX^{\mathrm{sh}}\to X^{\mathrm{sh}}$ has a point $t$ over the closed
point, and its residue field is a finite separable extension of the separably
closed residue field $\kappa$ of $R$, hence equal to $\kappa$. An affine open
neighbourhood $\Spec S$ of $t$ is étale over the henselian $R$, so there is a
retraction $S\to R$ of $R\to S$ ([Stacks, Tag 04GG](https://stacks.math.columbia.edu/tag/04GG), condition (8)), that is, a
section of $T\times_XX^{\mathrm{sh}}\to X^{\mathrm{sh}}$. Hence
$L|_{X^{\mathrm{sh}}}$ has a lattice $N$. Since
$X^{\mathrm{sh}}$ is strictly henselian, every finite étale cover of it splits,
so its fundamental group is trivial and by (1) $N\cong\mathcal
O_{E,X^{\mathrm{sh}}}^{\oplus r}$; hence $L|_{X^{\mathrm{sh}}}\cong
E^{\oplus r}_{X^{\mathrm{sh}}}$. By [det-lem-stratified-lattice-scheme] (1),
$T\times_XX^{\mathrm{sh}}$ is then the disjoint union of copies of
$X^{\mathrm{sh}}$ indexed by the lattices in $E^r$. Its open and closed
subscheme $T'\times_XX^{\mathrm{sh}}$ is a union of some of these copies, each
connected, and each copy has exactly one point over the generic point of
$X^{\mathrm{sh}}$. Over that generic point $T'\times_XX^{\mathrm{sh}}$ has exactly
one point, because $T'_U\cong U$. Hence $T'\times_XX^{\mathrm{sh}}\cong
X^{\mathrm{sh}}$.

Thus the étale morphism $T'\to X$ is surjective and each geometric fibre is a
single point, so it is universally injective. An étale universally injective
morphism is an open immersion ([Stacks, Tag 025G](https://stacks.math.columbia.edu/tag/025G)), and being surjective, $T'\to X$
is an isomorphism. Its inverse $X\to T'\subseteq T$ is a lattice $L_0\subseteq L$
on all of $X$. Normality was used three times: to make $X$ and the components
of $T$ irreducible, so that $T'_U=s(U)$, and to make $X^{\mathrm{sh}}$
irreducible, so that $T'\times_XX^{\mathrm{sh}}$ is a single copy.

Finally, a lisse $\QbarX$-module is $\QbarX\otimes_{E_X}L$ for a lisse
$E_X$-module $L$ and a finite $E$ ([det-lem-coefficient-finite-descent-lisse]
(1)), and $L$ has a lattice by the above, so it is integral.

*(5) Fields of definition.* Let $\sigma:\pi_1\to\GL_n(\Qlb)$ be continuous.
For each $d$, $\Ql$ has only finitely many extensions of degree $d$ inside
$\Qlb$ (a consequence of Krasner's lemma), so $\Qlb$ is the union of an
increasing sequence $E_1\subseteq E_2\subseteq\cdots$ of finite extensions
of $\Ql$. Each $E_m$ is complete, hence closed in $\Qlb$, so the subgroups
$\sigma^{-1}(\GL_n(E_m))$ are closed and cover the compact Hausdorff group
$\pi_1$. By the Baire category theorem one of them has nonempty interior;
being a subgroup, it is open, hence of finite index. Adjoining to $E_m$ the
matrix entries of $\sigma$ at finitely many coset representatives gives a
finite $E$ with $\sigma(\pi_1)\subseteq\GL_n(E)$. Then $V_E=E^n$ is
$\pi_1$-stable with $\Qlb\otimes_EV_E=\Qlb^n$, and $\pi_1$ acts on it
continuously, the topology of $E$ being the subspace topology from $\Qlb$.

The theorem follows from (3), (4) and (5): for regular, or more generally
normal, $X$ every lisse $\QbarX$-module is integral by (4), and every
continuous representation is defined over a finite $E$ by (5), so (3) is the
asserted equivalence.
