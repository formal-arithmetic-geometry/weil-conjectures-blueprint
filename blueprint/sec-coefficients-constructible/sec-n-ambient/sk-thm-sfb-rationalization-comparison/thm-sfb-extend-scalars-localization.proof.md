+++
kind  = "proof"
of    = "thm-sfb-extend-scalars-localization"
uses = ["lem-sfb-extend-scalars-bounded-constructible", "det-def-sfb-derived-extension-of-scalars", "sk-lem-integral-models"]
+++
Write $F=E\otimes^{\mathrm L}_{\cO_E}-$, $\mathcal T=D_{\mathrm{cons}}(X_{\mathrm{proét}},\cO_E)$
and $\mathcal T'=D_{\mathrm{cons}}(X_{\mathrm{proét}},E)$. By the proof of
[lem-sfb-extend-scalars-bounded-constructible], $F$ is induced by the exact functor
$E_X\otimes_{\cO_{E,X}}-$ with $E_X=\colim(\cO_{E,X}\xrightarrow{\ell}\cO_{E,X}\to\cdots)$.
So $F$ is triangulated.

*$F$ inverts $W_{\ell^{\mathbf N}}$.* If $\ell^n\cdot\mathrm{id}_Z=0$, then
$\ell^n\cdot\mathrm{id}_{F(Z)}=0$. But $\ell$ acts invertibly on $E_X$-modules, so
$F(Z)=0$. A morphism with $\ell$-power-torsion cone is therefore sent to a morphism with
zero cone, i.e. to an isomorphism. So $F$ factors through
$\bar F\colon\mathcal T[\ell^{-1}]\to\mathcal T'$.

*Morphisms of the rationalization.* For $s\colon L\to L'$ in $W_{\ell^{\mathbf N}}$ with
cone $C$ killed by $\ell^n$, the composite $L'\to C$ of $\ell^n\cdot\mathrm{id}_{L'}$ is
zero. So $\ell^n\cdot\mathrm{id}_{L'}=s\circ t$ for some $t\colon L'\to L$. Then
$s\circ(t\circ s-\ell^n)=0$, so $t\circ s-\ell^n$ factors through $C[-1]$ and is killed by
$\ell^n$, which gives $(\ell^nt)\circ s=\ell^{2n}$. Hence the multiplications by $\ell^n$
are cofinal in $W_{\ell^{\mathbf N}}$, and
$$
\Hom_{\mathcal T[\ell^{-1}]}(K,L)=\colim\bigl(\Hom_{\mathcal T}(K,L)\xrightarrow{\ell}\Hom_{\mathcal T}(K,L)\xrightarrow{\ell}\cdots\bigr)=\Hom_{\mathcal T}(K,L)[\ell^{-1}].
$$

*Full faithfulness of $\bar F$.* By the adjunction
$F\dashv D(\operatorname{Res}_\varphi)$ [det-def-sfb-derived-extension-of-scalars],
$\Hom_{\mathcal T'}(F(K),F(L))=\Hom(K,E_X\otimes_{\cO_{E,X}}L)$, and
$E_X\otimes_{\cO_{E,X}}L$ is the sequential homotopy colimit of $L\xrightarrow{\ell}L\to\cdots$.
So full faithfulness amounts to the commutation
$$
\colim_\ell\Hom(K,L)\xrightarrow{\ \sim\ }\Hom(K,\colim_\ell L)
$$
for bounded constructible $K,L$. By dévissage along the canonical truncations and the
common stratification of the proof of [det-def-sfb-bounded-constructible], one reduces to
$K$ a single locally finitely presented module on a stratum. There $\Hom(K,-)$ is
computed by pro-étale cohomology on a quasi-compact quasi-separated scheme (a
topologically Noetherian scheme is such), which commutes with filtered colimits
(Bhatt–Scholze, §6.8).

*Essential surjectivity.* By [sk-lem-integral-models] (4), every object of $\mathcal T'$
is obtained by finitely many cones and shifts from objects $F(a_!L_0)=(a_!L_0)[1/\ell]$
with $a_!L_0\in\mathcal T$. The essential image of $\bar F$ is closed under shifts, and it
is closed under cones by the description of the Hom groups: a morphism
$u\colon F(A)\to F(B)$ with $A,B\in\mathcal T$ is $\ell^{-c}F(v)$ for some $c\ge0$ and some
$v\colon A\to B$, and since $\ell^{-c}$ is an automorphism of $F(A)$, the cone of $u$ is
isomorphic to $F(\operatorname{cone}(v))$. So a connecting morphism between integral
generators lifts to an integral one after multiplication by a power of $\ell$, and
finite cones of the generators have integral models.

So $\bar F$ is an equivalence, i.e. $F$ is a localization at $W_{\ell^{\mathbf N}}$.
