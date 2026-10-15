+++
kind = "proof"
of = "det-pe-wcb-projective"
+++
Here $h_U$ is a sheaf by [det-pe-topos-functoriality-site].

*1.* An epimorphism of sheaves $\varphi\colon F\to h_U$ is locally surjective: for the
element $\mathrm{id}_U\in h_U(U)$ there are a covering $\{U_i\to U\}$ and elements
$a_i\in F(U_i)$ with $\varphi(a_i)=(U_i\to U)\in h_U(U_i)$. By
[det-pe-wcb-clopen-partition] there are a clopen partition $U=\bigsqcup_kU'_k$ and
$U$-morphisms $g_k\colon U'_k\to U_{i_k}$. Put $b_k=g_k^*a_{i_k}\in F(U'_k)$; then
$\varphi(b_k)$ is the inclusion $U'_k\to U$. The family $\{U'_k\to U\}$ is a (Zariski)
covering. Since the $U'_k$ are disjoint open subschemes, $U'_k\times_UU'_l=\emptyset$ for
$k\neq l$, and $U'_k\times_UU'_k=U'_k$; so the $b_k$ are trivially compatible and glue to
$b\in F(U)$ with $\varphi(b)|_{U'_k}=(U'_k\to U)$ for all $k$, hence $\varphi(b)=
\mathrm{id}_U$ by the sheaf property of $h_U$. By the Yoneda lemma, $b$ is a map
$h_U\to F$ with $\varphi\circ b=\mathrm{id}$.

*2.* Let $F\to G$ be an epimorphism and $y\in G(U)=\Hom(h_U,G)$. In a topos, pullbacks of
epimorphisms are epimorphisms, so $F\times_Gh_U\to h_U$ is an epimorphism; by 1 it has a
section, and composing with the projection to $F$ gives $x\in F(U)$ mapping to $y$.
