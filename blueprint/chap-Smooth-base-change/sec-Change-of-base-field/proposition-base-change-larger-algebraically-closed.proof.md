+++
kind = "proof"
of = "proposition-base-change-larger-algebraically-closed"
order = 689
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-underived-base-change-map", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "remark-base-change-compactification", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "lemma-rigidification-along-section", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-hilbert-schemes-points-smooth-curve", "lemma-representability-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "corollary-torsion-jacobian-field-extension", "lemma-cohomology-multiplicative-group", "proposition-cohomology-smooth-affine-curve", "lemma-p-torsion-affine-curve-characteristic", "lemma-finite-morphisms-cohomology"]
+++
We describe $R^qh_*$ as a sheafification and show that each local class
dies after a suitable étale covering. In degrees at least two this is
the cohomological dimension of affine curves. In degree one we first
descend the class to $C_L$, then trivialize it on a finite étale Galois
cover of $C_L$, and finally extend this cover over $C$.

*Step 1: reduction to local classes.* We may work on the étale
site, because $h$ is qcqs and direct images can be compared
(Theorem [theorem-comparison-direct-images]). There, [Stacks, [03Q8](https://stacks.math.columbia.edu/tag/03Q8)]
identifies $R^qh_*\underline{\mathbf Z/m}$ with the
sheafification of the presheaf

$$
U\longmapsto H^q(U\times_S\operatorname{Spec}\Omega,
\mathbf Z/m),
\qquad U\to C\text{ \'etale},
$$

so we must show that every such class vanishes on an étale covering
of $U$.

*Step 2: degrees $q\geq2$.* In these degrees the groups themselves
vanish for affine $U$, which we may assume because the question is local
on $U$. Indeed, $U_\Omega$ is then affine and étale over $C_\Omega$.
Hence it is empty or a finite disjoint union of smooth affine curves over
the algebraically closed field $\Omega$, and $(C_2)$ of
Theorem [theorem-cohomology-curves] kills its cohomology in
degrees $q\geq2$.

*Step 3: a section and connected fibres.* From now on $q=1$. The
extension theorem we want to use requires a section and geometrically
connected fibres. The map $U\to S$ need not have them, but we may arrange
them locally. By [Stacks, [0EY4](https://stacks.math.columbia.edu/tag/0EY4)], after an étale covering of $U$ the map
$U\to S$ factors as $U\to V\to S$ with $U$ and $V$ affine, $V\to S$ étale,
and $U\to V$ smooth with geometrically connected fibres and a section.
Moreover, the separated étale map $V\to S$ is a finite disjoint union of
open immersions [Stacks, [09Z9](https://stacks.math.columbia.edu/tag/09Z9)], because $S$ is normal and integral with
separably closed function field. As we only have to kill classes on
$U_\Omega$, we may therefore replace $S$ by one of these opens and $C$ by
the part of $U$ over it, which does not change the fraction field $L$.
Afterwards there
is a section $s:S\to C$ and the fibres are geometrically connected.

*Step 4: descent to $C_L$ and a trivializing cover.* Let
$\xi\in H^1(C_\Omega,\mathbf Z/m)$. It is the pullback of a unique class
$\xi_L\in H^1(C_L,\mathbf Z/m)$, because the pullback
$H^1(C_L,\mathbf Z/m)\to H^1(C_\Omega,\mathbf Z/m)$ is an isomorphism by
$(C_6)$ of Theorem [theorem-cohomology-curves], applied to the affine
curve $C_L$ as in [Stacks, [03SC](https://stacks.math.columbia.edu/tag/03SC)]; this step uses that $m$ is prime to the
characteristic. Next, the classification of $H^1$ by torsors [Stacks, [03AJ](https://stacks.math.columbia.edu/tag/03AJ)] and
Lemma [lemma-torsors-under-classical-groups] show that $\xi_L$ is the
class of a finite étale $\mathbf Z/m$-torsor $P\to C_L$. Choose a
connected component $Z$ of $P$ and let $G\subseteq\mathbf Z/m$ be its
stabilizer. As the curve $C_L$ is connected, $Z\to C_L$ is a finite
étale Galois cover with group $G$. The class $\xi_L$ vanishes on $Z$,
because the pullback of $P$ to $Z$ has the diagonal section.

*Step 5: extending the cover over $C$.* We use the extension theorem
for generic Galois covers [Stacks, [0EZJ](https://stacks.math.columbia.edu/tag/0EZJ)]: let $S$ be
integral, normal and qcqs with generic point $\eta$, and let $C\to S$
be qcqs and smooth with geometrically connected fibres and a section
$s$. If $Z\to C_\eta$ is a finite étale Galois cover with group
$G$ of order invertible on $S$, and $Z$ has a $\kappa(\eta)$-rational point
over $s(\eta)$, then $Z$ extends to a finite étale Galois cover
$\widetilde Z\to C$ with group $G$. The idea is that a cover of order
prime to the residue characteristics ramifies only tamely, and splitting over the section then rules out ramification
along the irreducible special fibres, and at points of codimension at least two
the cover extends by purity of the branch locus.

The hypotheses hold with $C_\eta=C_L$. Indeed, the order $|G|$ divides $m$
and is therefore invertible on $S$. Moreover, the fibre of $Z$ over
$s(\eta)$ is nonempty, as $Z\to C_L$ is finite étale and surjective, and
it has an $L$-rational point because $L$ is algebraically closed. So
$\widetilde Z$ exists.

We check that $\widetilde Z\to C$ is an étale covering, that is, that it
is surjective. The scheme $C$ is connected, since $C\to S$ is open and
surjective with connected fibres over a connected base. Hence
the image of $\widetilde Z$ in $C$, which is open and closed and contains the
generic fibre, is all of $C$. Finally, $\xi$ dies on this covering. Indeed,
$\widetilde Z\times_C C_\Omega=Z\times_{C_L}C_\Omega$, so the pullback of
$\xi$ to $\widetilde Z\times_CC_\Omega$ is the pullback of $\xi_L|_Z=0$.
