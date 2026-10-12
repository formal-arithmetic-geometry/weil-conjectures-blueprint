+++
id = "def-weil-locally-closed-subset"
kind = "definition"
title = "Locally closed subset"
refines = "def-weil-scheme-morphism-properties"
lean = ["IsLocallyClosed"]
tags = ["sheaf-dag", "mathlib", "stacks-004E"]
+++
Let $X$ be a topological space (for instance the underlying space of a scheme). A subset $E\subseteq X$ is *locally closed* if there are an open subset $U\subseteq X$ and a closed subset $Z\subseteq X$ with $E=U\cap Z$; equivalently, $E$ is open in its closure $\overline E$.
