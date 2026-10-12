+++
id = "def-weil-preadditive-category"
kind = "definition"
title = "Preadditive category"
lean = ["CategoryTheory.Preadditive"]
tags = ["sheaf-dag", "mathlib", "stacks-00ZY"]
+++
A *preadditive category* is a category $\mathcal C$ together with an abelian group structure on every set $\mathrm{Hom}(X,Y)$ such that composition is bilinear: $(g+g')\circ f=g\circ f+g'\circ f$ and $g\circ(f+f')=g\circ f+g\circ f'$. In particular $1-u:=\mathrm{id}_X-u$ is defined for every endomorphism $u$ of $X$.
