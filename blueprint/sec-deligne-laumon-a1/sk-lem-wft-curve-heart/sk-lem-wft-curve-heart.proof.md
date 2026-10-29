+++
kind  = "proof"
of    = "sk-lem-wft-curve-heart"
+++
The proof uses the largest punctual subsheaf of a constructible sheaf
to build the truncation triangles.

*Punctual subsheaves.* We first show that a lisse sheaf $L$ has no
nonzero punctual subsheaf. For a geometric point $\bar x$ and a
geometric generic point $\bar\eta$ specializing to it, the
generization map $L_{\bar x}\to L_{\bar\eta}$ is injective. For a
lisse sheaf on the smooth, hence normal, curve this follows from
[sk-p-real-integral]: on a connected
open containing both points, the stalks at $\bar x$ and $\bar\eta$ are
identified with the same representation of the fundamental group, and
the generization map is this identification. A punctual subsheaf $G\subset L$ has
$G_{\bar\eta}=0$, and since the generization maps of $G$ and $L$ are
compatible, $G_{\bar x}=0$. Now let $j:U\hookrightarrow C$ be a dense
open on which a constructible sheaf $F$ is lisse, and put

$$
 F_{\rm p}=\ker(F\longrightarrow j_*j^*F).
$$

It is supported on the finite set $C\setminus U$, hence punctual. A
punctual subsheaf $G$ of $F$ restricts to zero on $U$ by what we just
proved, so its map to $j_*j^*F$, being adjoint to $j^*G\to j^*F$,
vanishes and $G\subset F_{\rm p}$. Thus $F_{\rm p}$ is the largest
punctual subsheaf of $F$; in particular it does not depend on $U$ and
is preserved by Weil transport. Finally, $j_*j^*F$ has no nonzero
punctual subsheaf: if $H\subset j_*j^*F$ is punctual, then $j^*H=0$,
so the inclusion is zero since
$\operatorname{Hom}(H,j_*j^*F)=\operatorname{Hom}(j^*H,j^*F)=0$.
Hence $F/F_{\rm p}$, which embeds in $j_*j^*F$, has no nonzero
punctual subsheaf.

*The t-structure.* The shift axioms follow immediately from the
definitions. If $A\in{}^pD^{\le0}$ and $B\in{}^pD^{\ge1}$, then
ordinary truncation identifies $\operatorname{Hom}(A,B)$ with
$\operatorname{Hom}(\mathcal H^0A,\mathcal H^0B)$, which is zero
because the source is punctual and the target has no punctual
subsheaf. To construct the truncation triangle for $K$, put
$K'=\tau^{\le0}K$ and $F=\mathcal H^0K$, and let $A$ be the fibre of
$K'\to F/F_{\rm p}$. The cohomology of $A$ is that of $K$ below zero,
and $\mathcal H^0A=F_{\rm p}$, so that $A\in{}^pD^{\le0}$. By the
octahedral axiom we obtain a triangle $A\to K\to B\to$ in which $B$
has no negative ordinary cohomology and $\mathcal H^0B=F/F_{\rm p}$,
and hence $B\in{}^pD^{\ge1}$. The t-structure is bounded because the
ordinary one is.

*The heart.* The heart of any t-structure is abelian, with kernels and
cokernels computed from the perverse cohomology of a cone
([BBD, Théorème 1.3.6]); the proof uses only the octahedral axiom and
orthogonality. Its objects have the stated form by definition.
Punctual sheaves belong to the heart, and so does $(j_*M)[1]$, since
$j_*M$ has no punctual subsheaf.

*Weil structures.* Frobenius pullback is an exact equivalence for the
ordinary t-structure, and it preserves punctual support and the
absence of punctual subsheaves. It is therefore t-exact for the
geometric t-structure defined above. Since Frobenius pullback is
t-exact, it carries the kernel and cokernel of a compatible morphism
in the heart to the kernel and cokernel of the pulled-back morphism.
Hence the Weil isomorphisms and their inverses induce inverse
isomorphisms on the kernel and cokernel, and by naturality the
coimage–image map is compatible with them. We conclude that perverse
Weil sheaves form an abelian category and that the forgetful functor
to perverse sheaves on $C$ is exact and reflects exactness.
