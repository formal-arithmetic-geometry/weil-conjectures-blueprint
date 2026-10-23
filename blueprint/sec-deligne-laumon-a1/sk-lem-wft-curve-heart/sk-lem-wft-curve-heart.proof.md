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
does not depend on $U$, and it commutes with Weil transport.

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
The t-structure is bounded because the ordinary one is.

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

It remains to treat Weil structures. Frobenius pullback is an exact
equivalence for the ordinary t-structure, and it preserves punctual
support and the absence of punctual subsheaves. It is therefore
t-exact for the geometric t-structure defined above.
For a compatible morphism in the heart, exactness identifies the
pullbacks of its kernel and cokernel with those of the pulled-back
morphism. Hence the Weil isomorphisms and their inverses induce
inverse isomorphisms on the kernel and cokernel, and by naturality the
coimage–image map is compatible with them. We conclude that the
equivariant heart is abelian and that its forgetful functor is exact
and reflects exactness.
