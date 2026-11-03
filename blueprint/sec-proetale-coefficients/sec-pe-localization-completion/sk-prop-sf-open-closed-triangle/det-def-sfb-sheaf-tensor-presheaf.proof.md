+++
kind = "proof"
of = "det-def-sfb-sheaf-tensor-presheaf"
+++
**Monoidal structure.** The associator, unitors and symmetry are defined objectwise; they are
natural in $U$ because those of $\mathcal A$ are natural, and the pentagon, triangle and hexagon
identities hold because they hold at each $U$.

**Existence of the end.** Since $C$ is essentially small, so is $C/U$, and the end is the
equalizer of two maps between products over a set of objects, respectively of arrows, of $C/U$.
A Grothendieck abelian category has all small limits, so the end exists. Functoriality in $U$ is
induced by composition $C/U'\to C/U$, $(V\to U')\mapsto(V\to U'\to U)$.

**Hom formula.** By the universal property of the end and the tensor–hom adjunction of
$\mathcal A$, a map $A\to[F,G](U)$ is a family of maps
$A\to\underline{\Hom}_{\mathcal A}(F(V),G(V))$, i.e. maps $F(V)\otimes A\to G(V)$, indexed by
$(V\to U)$ and satisfying the wedge condition, which is naturality in $(V,v)$.

**Closedness.** A morphism $\psi\colon H\to[F,G]$ is a family of maps $\psi_U\colon H(U)\to[F,G](U)$
natural in $U$. By the Hom formula with $A=H(U)$, $\psi_U$ is a natural family
$\varphi^U_v\colon F(V)\otimes H(U)\to G(V)$ indexed by $(v\colon V\to U)\in C/U$. Naturality of
$\psi$ along $u\colon U'\to U$ says $\varphi^{U'}_{v'}\circ(F(V)\otimes H(u))=\varphi^U_{u\circ v'}$
for all $v'\colon V\to U'$. Taking $U'=V$, $u=v$, $v'=\mathrm{id}_V$ gives
$$
\varphi^U_v=\chi_V\circ\bigl(F(V)\otimes H(v)\bigr),\qquad \chi_V:=\varphi^V_{\mathrm{id}_V}\colon F(V)\otimes H(V)\to G(V).
$$
Naturality of $\varphi^U$ in $(V,v)$ then says exactly that $\chi$ is natural in $V$, i.e. a
morphism $\chi\colon F\otimes_pH\to G$. Conversely, a morphism $\chi$ defines $\varphi^U_v$ by the
displayed formula, natural in $(V,v)$ and in $U$. The two constructions are inverse, and natural
in $F,G,H$. So $\Hom(F\otimes_pH,G)\cong\Hom(H,[F,G])$.
