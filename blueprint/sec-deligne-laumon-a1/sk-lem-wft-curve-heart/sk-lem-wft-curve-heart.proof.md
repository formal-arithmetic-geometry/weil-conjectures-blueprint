+++
kind  = "proof"
of    = "sk-lem-wft-curve-heart"
+++
We first show that a lisse sheaf has no punctual subsheaf. For a lisse
sheaf, the generization map from a geometric stalk to a compatible
local geometric generic fibre is injective. For a sheaf defined over a
finite extension $E$ of $\Ql$, this holds for the finite locally
constant reductions of the lattice in [sk-p-real-integral], and we
pass to the inverse limit, invert the uniformizer and extend scalars.
If $j:U\hookrightarrow C$ is a dense open on which a constructible
sheaf $F$ is lisse, then

$$
 F_{\rm p}=\ker(F\longrightarrow j_*j^*F)
$$

is its largest punctual subsheaf, and the quotient $F/F_{\rm p}$ has
no punctual subsheaf, since it embeds in $j_*j^*F$. This description
does not depend on $U$, and it commutes with Weil transport. Hence for
a Weil sheaf $F$ on $C_0$, $F_{\rm p}$ is a Weil subsheaf, and it is
also the largest punctual Weil subsheaf; in particular $F$ has no
nonzero punctual Weil subsheaf exactly when its underlying sheaf has
no nonzero punctual subsheaf. We give the argument for Weil complexes;
the geometric case is the same without the Weil structures.

The shift axioms follow immediately from the definitions. If
$A\in{}^pD^{\le0}$ and $B\in{}^pD^{\ge1}$, then ordinary truncation
identifies $\operatorname{Hom}(A,B)$ with
$\operatorname{Hom}(\mathcal H^0A,\mathcal H^0B)$, which is zero because the source
is punctual and the target has no punctual subsheaf.
To construct the truncation triangle for $K$, put $K'=\tau^{\le0}K$
and $F=\mathcal H^0K$, and let $A$ be the fibre of
$K'\to F/F_{\rm p}$. The cohomology of $A$ is that of $K$ below zero,
and $\mathcal H^0A=F_{\rm p}$, so that $A\in{}^pD^{\le0}$.
By the octahedral axiom we obtain a triangle $A\to K\to B\to$ in which
$B$ has no negative ordinary cohomology and
$\mathcal H^0B=F/F_{\rm p}$. Thus $B\in{}^pD^{\ge1}$.
The t-structure is bounded because the ordinary one is. As for any
t-structure, ${}^pD^{\ge0}$ is then the right orthogonal of
${}^pD^{\le-1}$: if $K$ receives no nonzero map from ${}^pD^{\le-1}$,
the first map of a triangle $A\to K\to B\to$ with
$A\in{}^pD^{\le-1}$ and $B\in{}^pD^{\ge0}$ (the shifted truncation
triangle) vanishes, so $K$ is a direct summand of $B$, and the
conditions defining ${}^pD^{\ge0}$ pass to direct summands.

To see that the heart is abelian, let $h:A\to B$ be a morphism in the
heart and choose a triangle $A\xrightarrow{h}B\to C_h\to A[1]$.
Then $C_h$ has perverse amplitude $[-1,0]$. Put
$K={}^p\mathcal H^{-1}(C_h)$ and $Q={}^p\mathcal H^0(C_h)$.
Applying orthogonality to this triangle and to
$K[1]\to C_h\to Q\to K[2]$, we identify $K\to A$ with the kernel
of $h$ and $B\to Q$ with its cokernel. The octahedral axiom for
$K\to C_h[-1]\to A$ gives an object $I$ and triangles

$$
 K\longrightarrow A\longrightarrow I\longrightarrow K[1],
 \qquad
 I\longrightarrow B\longrightarrow Q\longrightarrow I[1],
$$

whose composite $A\to I\to B$ is $h$. The first triangle puts $I$ in
${}^pD^{[-1,0]}$ and the second puts it in ${}^pD^{[0,1]}$, so $I$
lies in the heart. By orthogonality, $I$ is both
$\operatorname{coker}(K\to A)$ and $\ker(B\to Q)$.
Thus coimage equals image, and the heart is abelian. Its objects have
the stated form by definition. Punctual sheaves belong to the heart,
and so does $(j_*M)[1]$, since $j_*M$ has no punctual subsheaf.

All steps use only the cohomology Weil sheaves, their supports, the
punctual Weil subsheaf $F_{\rm p}$ of the first paragraph, the
ordinary truncations and the octahedral axiom in the triangulated
category of Weil complexes, so they hold verbatim there.
