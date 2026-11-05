+++
kind = "proof"
of = "lemma-extending-isomorphism-over-closure-closed--1"
order = 1452002
uses = ["lemma-separation-closures", "theorem-elimination-indeterminacy", "lemma-products-composites-u-admissible-blow", "lemma-schematic-closure-uniqueness"]
+++
Let $M\subseteq T$ be the largest open over which $q$ is an
isomorphism. In the spectral space $V$, enlarge the disjoint closed
sets $F$ and $V\setminus M$ to disjoint constructible closed sets
$F_c$ and $E_c$. Then $V_2=V\setminus E_c$ is quasi-compact and $q$
is an isomorphism over $V_2$. By [lemma-separation-closures], choose a
$V$-admissible blow-up $\pi_1:T_1=\Bl_{\mathcal I}(T)\to T$ such that
$\overline{\pi_1^{-1}(F_c)}$ and $\overline{\pi_1^{-1}(E_c)}$ are
disjoint.

Apply constructible separation a second time, now to these two closed
subsets of $T_1$. The complement of the second constructible enlargement
is a quasi-compact open $A\subseteq T_1$ satisfying

$$
\overline{\pi_1^{-1}(F)}\subseteq A,\qquad
A\cap\pi_1^{-1}(V)\subseteq\pi_1^{-1}(V_2).
$$

This is `AlgebraicGeometry.isoNearClosureNbhd`. The second separation
ensures that the open from which we later extend the centre is
quasi-compact.

The canonical lift
$\lambda_1:\Bl_{\mathcal I\mathcal O_P}(P)\to T_1$ is proper and is
an isomorphism over $\pi_1^{-1}(V_2)$. Apply
[theorem-elimination-indeterminacy] to this lift on $T_1$, preserving
$\pi_1^{-1}(V_2)$. This gives a blow-up with finite type centre
$\mathcal J$ whose strict transform of $\lambda_1$ is an open
immersion. The restriction $\mathcal J|_A$ has support disjoint from
$A\cap\pi_1^{-1}(V)$. Extend it to a finite type ideal $\mathcal D$
on $T_1$ whose support avoids all of $\pi_1^{-1}(V)$, using
`AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq_of_disjoint`.
Here the extension form underlying
[lemma-products-composites-u-admissible-blow] is used on the two
quasi-compact opens $A$ and $\pi_1^{-1}(V)$; $A$ need not contain
$\pi_1^{-1}(V)$.

The composition theorem
`AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comp_base_change`
gives a finite type centre $\mathcal K$ on $T$ for
$\Bl_{\mathcal D}(T_1)\to T_1\to T$, together with the corresponding
identification after pulling the centres back along $q$. Its support is

$$
\operatorname{Supp}(\mathcal K)
=\operatorname{Supp}(\mathcal I)
\cup\pi_1\bigl(\operatorname{Supp}(\mathcal D)\bigr),
$$

so it avoids $V$. Thus $b:\Bl_{\mathcal K}(T)\to T$ is the required
$V$-admissible blow-up.

It remains to verify the assertion about its strict transform. By
`AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_comap_iso_strictTransform`,
identify $P'$ with $\Bl_{\mathcal K\mathcal O_P}(P)$. Localizing the
canonical lifts over $A$, where $\mathcal D$ and $\mathcal J$ agree,
and using the composition identifications gives an open immersion
$m:W\to P'$ such that $j=q'\circ m:W\to T'$ is an open immersion
and

$$
m(W)=(q')^{-1}(j(W)).
$$

The image of $q'$ is closed, since $q'$ is proper, and it contains
$b^{-1}(F)$ because $q$ is an isomorphism near $F$. Hence it contains
$\overline{b^{-1}(F)}$. This closure also lies over $A$, by continuity
and the choice of $A$, so the localized comparison shows that it lies
in $j(W)$. Set $N'=j(W)$. The displayed equality and the two open
immersions identify $(q')^{-1}(N')\to N'$ with an isomorphism, as in
`AlgebraicGeometry.isIso_morphismRestrict_opensRange_of_range_eq`.
These final comparisons are packaged in
`AlgebraicGeometry.exists_isIso_strictTransformMap_of_isoNearClosureData`.
