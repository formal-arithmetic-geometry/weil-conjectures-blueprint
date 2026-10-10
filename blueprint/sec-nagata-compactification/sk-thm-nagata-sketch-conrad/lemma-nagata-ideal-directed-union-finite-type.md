+++
id = "lemma-nagata-ideal-directed-union-finite-type"
kind = "lemma"
title = "An ideal is the directed union of its finite type subideals, [stacks-project]"
order = 205
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.directedOn_ofFiniteType_le", "AlgebraicGeometry.Scheme.IdealSheafData.exists_ofFiniteType_le_comap_eq_top_of_le", "AlgebraicGeometry.Scheme.IdealSheafData.sSup_ofFiniteType_le_comap_eq_top_eq", "AlgebraicGeometry.Scheme.IdealSheafData.sSup_ofFiniteType_le_eq"]
uses = ["def-nagata-extended-ideal", "lemma-nagata-dense-flat-pullback", "lemma-nagata-finite-type-ideal-extension-exists"]
+++
Let $X$ be qcqs and let $\mathcal H\subseteq\mathcal O_X$ be a quasi-coherent
ideal. The finite type quasi-coherent subideals of $\mathcal H$ form a family
which is directed under inclusion and whose union is $\mathcal H$.

Suppose moreover that $U\subseteq X$ is a quasi-compact open with
$\mathcal H|_U=\mathcal O_U$. Then the subfamily of those finite type
subideals $\mathcal K\subseteq\mathcal H$ with $\mathcal K|_U=\mathcal O_U$ is
nonempty, is directed, and still has union $\mathcal H$; in particular every
finite type subideal of $\mathcal H$ is contained in a member of it.
