+++
id = "def-pc-representable-functor"
kind = "definition"
title = "Representable functors"
lean = ["CategoryTheory.Functor.isRepresentable_iff_exists_nonempty_iso"]
order = 625
uses = ["def-pc-scheme"]
+++
Let $F:(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$ be a functor. The
*functor of points* of a scheme $X$ over $S$ is
$h_X=\operatorname{Hom}_S(\bullet,X)$; $F$ is *representable by a
scheme* if $F\cong h_P$ for some scheme $P$ over $S$. A scheme
representing a functor is denoted $\underline{\operatorname{Pic}}$,
$\underline{\operatorname{Hilb}}$ etc.; uniqueness of the representing scheme is
[lem-pc-representable-unique].
