+++
kind = "proof"
of = "det-sp-reduction-compatibilities"
+++
(1) Both sides are morphisms $M_B\to f_B^!Rf_{!,B}(M_B)$; compare their
transposes under $Rf_{!,B}\dashv f_B^!$. The transpose of $\eta_B(M_B)$ is
$\mathrm{id}$. The transpose of the left side is
$\varepsilon_B(Rf_{!,B}M_B)\circ Rf_{!,B}f_B^!(b(M))\circ Rf_{!,B}(c_{A,B}(Rf_{!,A}M))\circ Rf_{!,B}((\eta_A M)_B)$;
by naturality of $\varepsilon_B$ this is
$b(M)\circ\varepsilon_B((Rf_{!,A}M)_B)\circ Rf_{!,B}(c_{A,B}(Rf_{!,A}M))\circ Rf_{!,B}((\eta_AM)_B)$.
By the defining identity of $c_{A,B}$ and naturality of $b$ this equals
$b(M)\circ(\varepsilon_A(Rf_{!,A}M))_B\circ b(f_A^!Rf_{!,A}M)^{-1}\circ Rf_{!,B}((\eta_AM)_B)
=b(M)\circ\bigl(\varepsilon_A(Rf_{!,A}M)\circ Rf_{!,A}(\eta_AM)\bigr)_B\circ b(M)^{-1}$,
which is $\mathrm{id}$ by the triangle identity over $A$.

(2) Compute transposes under $Rf_{!,C}\dashv f_C^!$. Applying the defining
identity for $c_{B,C}$ and then (the scalar extension to $C$ of) the identity
for $c_{A,B}$, the transpose of the composite is
$(\varepsilon_A(K))_C\circ$ (the composite of $b$ for $A\to B$ extended to $C$
and $b$ for $B\to C$)$^{-1}$, modulo associativity isomorphisms. By the
cocycle property of $b$ ([det-sp-reduction-direct-image]) this is
$(\varepsilon_A(K))_C\circ b_{A,C}^{-1}$, the transpose of $c_{A,C}(K)$. Hence the
two maps are equal.

(3) $\gamma_{f,A}(K)$ is the tensor map
$f_A^*K\otimes^{\mathbf L}\omega_{f,A}\to f_A^!K$ (the transpose of the
projection formula followed by the counit) composed with the inverse of the
orientation $\omega_{f,A}\simeq A_X(d)[2d]$. *Tensor map:* its transpose is
built from the projection formula and $\varepsilon_A$; the projection formula
commutes with extension of scalars (both are associativity and counit maps,
compatible with $b$), and $\varepsilon$ is compatible by the defining identity
of $c_{A,B}$; so the tensor maps over $A$ and $B$ correspond under $c_{A,B}$.
*Orientation:* the orientation of [thm-pur-diagonal-dualizing-object] comes
from deformation to the normal bundle, whose geometry does not depend on
coefficients; its rank-one sheaves are locally free, so their derived
extensions are ordinary ones even when $A\to B$ is not flat. On the
deformation family the comparisons at $t=1$ are the chart comparisons of
[det-sp-reduction-exceptional], so the scalar-extended comparison over $A$ and
the comparison over $B$ agree at $t=1$; by the uniqueness in the deformation
lemma (a comparison of rank-one locally constant sheaves normalized at $t=1$
is unique) they agree at $t=0$. Combining, $c_{A,B}(K)\circ(\gamma_{f,A}(K))_B=\gamma_{f,B}(K_B)$.
