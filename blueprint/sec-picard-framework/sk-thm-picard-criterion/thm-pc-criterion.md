+++
id = "thm-pc-criterion"
kind = "theorem"
title = "The representability criterion"
order = 835
uses = ["def-pc-cover", "def-pc-open-subfunctor", "def-pc-representable-functor", "def-pc-subfunctor", "def-pc-zariski-sheaf-property"]
lean = ["AlgebraicGeometry.isRepresentable_of_representable_open_subfunctor"]
+++
Let $k$ be a field and let
$G:(\mathit{Sch}/k)^{\mathrm{op}}\to\textit{Groups}$ be a functor. With the
terminology of
Definition [def-pc-subfunctor], assume:

1. **(1)** $G$ satisfies the sheaf property for the Zariski topology ([def-pc-zariski-sheaf-property]),
and its values $G(T)$ are small, i.e. lie in the same universe as the $k$-schemes $T$;
1. **(2)(a)** there exists a subfunctor $F\subseteq G$ such that $F$ is
representable;
1. **(2)(b)** $F\subseteq G$ is representable by open immersions ([def-pc-open-subfunctor]);
1. **(2)(c)** for every field extension $K$ of $k$ and every
$g\in G(K)$ there exists $g'\in G(k)$ such that $g'g\in F(K)$.

Then $G$ is representable by a group scheme over $k$.
