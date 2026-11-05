+++
kind = "proof"
of = "sk-thm-vanishing"
uses = ["sk-thm-curve-package", "sk-lem-pe-torsor-comparison", "sk-prop-input-spreading", "sk-prop-input-torsors", "sk-prop-normal-form", "sk-thm-pe-direct-image-comparison"]
+++
Since $h$ is qcqs, the comparison of direct images
(Theorem [sk-thm-pe-direct-image-comparison]) lets us work on the étale site. By
[Stacks, Tag 03Q8](https://stacks.math.columbia.edu/tag/03Q8), the sheaf $R^qh_*\underline{\mathbf Z/m}$ is the
sheafification of the presheaf

$$
U\longmapsto H^q(U\times_S\operatorname{Spec}\Omega,
\mathbf Z/m),
\qquad U\to C\text{ \'etale},
$$

so we must show that every such class vanishes on an étale covering
of $U$. For $q\geq2$ the groups are already zero. For $q=1$ they can be
nonzero, and we kill a class by extending the corresponding torsor
from the generic fibre to a finite étale cover of the curve.

Since the question is local on $U$, we may take $U$ affine. Then $U_\Omega$ is empty or a smooth affine
curve over the algebraically closed field $\Omega$, and so its cohomology in
degrees $q\geq2$ vanishes by $(C_2)$ of Theorem [sk-thm-curve-package].

Now let $q=1$. By [Stacks, Tag 0EY4](https://stacks.math.columbia.edu/tag/0EY4), after an étale covering of $U$ the map
$U\to S$ factors as $U\to V\to S$ with $U$ and $V$ affine, $V\to S$ étale,
and $U\to V$ smooth with geometrically connected fibres and a section.
Since $S$ is normal and integral with separably closed function field,
the separated étale map $V\to S$ is a finite disjoint union of open
immersions [Stacks, Tag 09Z9](https://stacks.math.columbia.edu/tag/09Z9). Since we only have to kill classes on $U_\Omega$,
we may replace $S$ by one of these opens and $C$ by the part of $U$
over it. This does not change the fraction field $L$, and
afterwards there is a section $s:S\to C$ and the fibres are
geometrically connected.

Let $\xi\in H^1(C_\Omega,\mathbf Z/m)$. Since
$m$ is prime to the characteristic, $(C_6)$ of
Theorem [sk-thm-curve-package], applied to the affine
curve $C_L$ as in [Stacks, Tag 03SC](https://stacks.math.columbia.edu/tag/03SC), shows that the pullback
$H^1(C_L,\mathbf Z/m)\to H^1(C_\Omega,\mathbf Z/m)$ is an isomorphism. Thus $\xi$
is the pullback of a unique class $\xi_L\in H^1(C_L,\mathbf Z/m)$.
By the classification of $H^1$ by torsors [Stacks, Tag 03AJ](https://stacks.math.columbia.edu/tag/03AJ) and
Lemma [sk-lem-pe-torsor-comparison], $\xi_L$ is the class of a finite
étale $\mathbf Z/m$-torsor $P\to C_L$. Choose a connected component $Z$
of $P$ and let $G\subseteq\mathbf Z/m$ be its stabilizer. Since the curve
$C_L$ is connected, $Z\to C_L$ is a finite étale Galois cover with
group $G$. The pullback of $P$ to $Z$ has the diagonal section, and
hence $\xi_L$ vanishes on $Z$.

It remains to extend $Z$ over all of $C$. Recall the extension theorem
for generic Galois covers [Stacks, Tag 0EZJ](https://stacks.math.columbia.edu/tag/0EZJ): let $S$ be
integral, normal and qcqs with generic point $\eta$, and let $C\to S$
be qcqs and smooth with geometrically connected fibres and a section
$s$. If $Z\to C_\eta$ is a finite étale Galois cover with group
$G$ of order invertible on $S$, and $Z$ has a $\kappa(\eta)$-rational point
over $s(\eta)$, then $Z$ extends to a finite étale Galois cover
$\widetilde Z\to C$ with group $G$. The reason is that a cover of order
prime to the residue characteristics ramifies only tamely, and splitting
over the section rules out ramification along the irreducible special
fibres; at points of codimension at least two the cover extends by
purity of the branch locus.

We check the hypotheses, with $C_\eta=C_L$. The order $|G|$ divides $m$
and is therefore invertible on $S$. Since $Z\to C_L$ is finite étale
and surjective, its fibre over $s(\eta)$ is nonempty, and it has an
$L$-rational point because $L$ is algebraically closed. Hence
$\widetilde Z$ exists. The scheme $C$ is connected, since $C\to S$ is open
and surjective with connected fibres over a connected base. The image of
$\widetilde Z$ in $C$ is open and closed and contains the generic fibre, and
so $\widetilde Z\to C$ is surjective, that is, an étale covering. Finally,
$\widetilde Z\times_C C_\Omega=Z\times_{C_L}C_\Omega$, and so the pullback of $\xi$
to $\widetilde Z\times_CC_\Omega$ is the pullback of $\xi_L|_Z=0$. Thus every
class in degree one vanishes locally on $C$.
