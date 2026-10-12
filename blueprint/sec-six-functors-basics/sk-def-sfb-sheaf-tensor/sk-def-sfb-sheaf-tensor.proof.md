+++
kind  = "proof"
of    = "sk-def-sfb-sheaf-tensor"
+++
**$\Ab$.** The tensor product of abelian groups is the tensor product of
$\mathbf Z$-modules: it is associative, unital with unit $\mathbf Z$, and symmetric, and
it is additive in each variable. The tensor–hom adjunction
$\Hom(M\otimes_{\mathbf Z}N,P)\cong\Hom(N,\Hom(M,P))$ makes it closed. $\Ab$ is
Grothendieck abelian.

**Presheaves.** The category of $\mathcal A$-valued presheaves on $C$ is symmetric
monoidal for the objectwise tensor product. It is closed: the internal hom $[F,G]$ is
the end $[F,G](U)=\int_{V\to U}\Hom_{\mathcal A}(F(V),G(V))$, taken over the objects
$V\to U$ of $C/U$. This end is a limit indexed by a category of the size of $C$. It
exists because $\mathcal A$, being Grothendieck abelian, has all limits of that size,
and here the smallness assumption on $C$ is used. If $G$ is a sheaf, then $[F,G]$ is a
sheaf.

**Monoidal structure on sheaves.** Let $W$ be the class of morphisms of presheaves that
sheafification inverts. Equivalently, $g\in W$ when $\Hom(g,H)$ is bijective for every
sheaf $H$. The class $W$ is stable under $F\otimes-$: for $g\in W$ and a sheaf $H$,
$\Hom(F\otimes g,H)\cong\Hom(g,[F,H])$, which is bijective because $[F,H]$ is a sheaf.
The braiding transports this to $-\otimes F$. Hence the monoidal structure on presheaves
descends to the localization at $W$. Sheafification identifies this localization with
$\Sh(C,\mathcal A)$. So $\Sh(C,\mathcal A)$ inherits a monoidal structure for which
sheafification is strong monoidal. On sheaves it is given by
$\mathcal F\otimes\mathcal G=a(\mathcal F\otimes\mathcal G)$, and its unit is
$a(\underline{\mathbf 1})$. The braiding and the symmetry descend in the same way. This
proves 1.

**Closedness.** The sheafification adjunction $a\dashv\iota$ exhibits $\Sh(C,\mathcal A)$
as a reflective subcategory of a symmetric monoidal closed category, and the reflector
$a$ is strong monoidal. By Day's reflection theorem, $\Sh(C,\mathcal A)$ is then
monoidal closed, with $\mathcal{H}om(\mathcal F,\mathcal G)=[\mathcal F,\mathcal G]$ for
sheaves $\mathcal F,\mathcal G$. So $\mathcal F\otimes-$ is a left adjoint and preserves
colimits. By the symmetry, so does $-\otimes\mathcal F$. This proves 2.

For $\mathcal A=\Ab$, apply this to the closed symmetric monoidal structure
$\otimes_{\mathbf Z}$ of the first paragraph.
