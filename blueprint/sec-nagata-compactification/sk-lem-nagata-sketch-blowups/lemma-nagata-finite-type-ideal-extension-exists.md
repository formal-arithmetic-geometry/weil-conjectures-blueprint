+++
id = "lemma-nagata-finite-type-ideal-extension-exists"
kind = "lemma"
title = "Existence of a finite-type extension of an ideal"
order = 126
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq", "AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_le_comap_eq"]
uses = ["def-nagata-extended-ideal"]
+++
Let $X$ be quasi-compact and quasi-separated and let $W\subseteq X$ be a
quasi-compact open.

1. If $\mathcal J\subseteq\mathcal O_W$ is a finite type quasi-coherent
   ideal, there exists a finite type quasi-coherent ideal
   $\mathcal I\subseteq\mathcal O_X$ with $\mathcal I|_W=\mathcal J$.
2. If $\mathcal H\subseteq\mathcal O_X$ is a quasi-coherent ideal whose
   restriction $\mathcal H|_W$ is of finite type, there exists a finite type
   quasi-coherent ideal $\mathcal I\subseteq\mathcal H$ with
   $\mathcal I|_W=\mathcal H|_W$.

More generally, both assertions hold for quasi-coherent submodules of a
quasi-coherent $\mathcal O_X$-module $\mathcal F$ in place of ideals of
$\mathcal O_X$: a quasi-coherent submodule $\mathcal H\subseteq\mathcal F$
with $\mathcal H|_W$ of finite type contains a finite type quasi-coherent
submodule with the same restriction to $W$, and every finite type
quasi-coherent submodule $\mathcal G\subseteq\mathcal F|_W$ is the
restriction of a finite type quasi-coherent submodule of $\mathcal F$.
