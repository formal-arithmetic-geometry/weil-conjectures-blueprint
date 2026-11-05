+++
kind = "proof"
of = "proposition-cohomology-p-1-over-henselian--1"
order = 375002
uses = ["theorem-comparison-over-henselian-pair-degree", "lemma-cohomology-modules-underlying-abelian", "lemma-acyclicity-closed-fibre"]
+++
We argue by induction on $q$, for all sheaves of $\mathbf F_\ell$-modules
at once. In degree zero, the assertion is
[theorem-comparison-over-henselian-pair-degree], applied to the proper
scheme $\mathbf P^1_R$ over the henselian pair $(R,\m_R)$.

For the induction step, embed $F$ into an injective sheaf $I$ of
$\mathbf F_\ell$-modules and put $C=I/F$. Forgetting the module structure
and then applying the exact functor $i^*$ gives two short exact sequences
of abelian sheaves. The underlying abelian sheaf of $I$ has no positive
cohomology, as in [lemma-cohomology-modules-underlying-abelian], and
$I_0$ has no positive cohomology by [lemma-acyclicity-closed-fibre].
Thus the two long exact sequences give a commutative diagram with exact
rows

$$
\begin{array}{ccccc}
H^q(\mathbf P^1_R,I)&\longrightarrow&H^q(\mathbf P^1_R,C)
&\longrightarrow&H^{q+1}(\mathbf P^1_R,F)\longrightarrow0\\
\downarrow&&\downarrow&&\downarrow\\
H^q(\mathbf P^1_\kappa,I_0)&\longrightarrow&H^q(\mathbf P^1_\kappa,C_0)
&\longrightarrow&H^{q+1}(\mathbf P^1_\kappa,F_0)\longrightarrow0.
\end{array}
$$

Restriction commutes with the maps of the short exact sequences and with
the connecting maps. The first two vertical maps are isomorphisms by the
induction hypothesis. The induced map on their cokernels is therefore an
isomorphism, which proves the assertion in degree $q+1$.
