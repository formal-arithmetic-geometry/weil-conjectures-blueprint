+++
id = "lem-weil-pbc-counit-stalk-germ-restriction"
kind = "lemma"
title = "The stalk of the counit $f^{-1}f_*F\\to F$ is the restriction of germs"
uses = ["def-pc-scheme", "def-weil-pbc-abelian-etale-sheaves", "def-weil-geometric-point", "def-weil-pbc-geometric-stalks", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "lem-weil-pbc-inverse-image-stalk-germ"]
refines = "proof/lem-weil-pbc-finite-pushforward-constructible-descent"
lean = ["branch", "declarations", "note"]
tags = ["sheaf-dag", "stacks-03Q1"]
+++
Let $f:X\to Y$ be a morphism of schemes [def-pc-scheme], $F$ an abelian sheaf on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves], $\bar x:\operatorname{Spec}\Omega\to X$ a geometric point [def-weil-geometric-point] and $\bar y=f\circ\bar x$. For a pointed etale neighbourhood $(V,\bar v)$ of $\bar y$ [def-weil-pbc-geometric-stalks], the pair $(V\times_YX,(\bar v,\bar x))$ is a pointed etale neighbourhood of $\bar x$ (the base change $V\times_YX\to X$ is etale, and $(\bar v,\bar x)$ is defined since $f\circ\bar x=\bar y$ is the image of $\bar v$), functorially in $(V,\bar v)$; since $(f_*F)(V)=F(V\times_YX)$ [def-weil-pbc-direct-image], these give a homomorphism of abelian groups $r_{f,\bar x,F}:(f_*F)_{\bar y}\to F_{\bar x}$ sending the germ of $s\in(f_*F)(V)$ at $(V,\bar v)$ to the germ of $s\in F(V\times_YX)$ at $(V\times_YX,(\bar v,\bar x))$. Let $\varepsilon_{f,F}:f^{-1}f_*F\to F$ be the counit of the adjunction $f^{-1}\dashv f_*$ [def-weil-pbc-inverse-image] and $c_{f,\bar x,f_*F}:(f^{-1}f_*F)_{\bar x}\xrightarrow{\sim}(f_*F)_{\bar y}$ the isomorphism of [lem-weil-pbc-inverse-image-stalk-germ] (for the sheaf $G=f_*F$ on $Y$). Then the stalk of the counit at $\bar x$ is
$$(\varepsilon_{f,F})_{\bar x}=r_{f,\bar x,F}\circ c_{f,\bar x,f_*F}:(f^{-1}f_*F)_{\bar x}\longrightarrow F_{\bar x}.$$
(No finiteness of $f$ is needed. Proof in outline, for the split: for $s\in(f_*F)(V)$ the triangle identity $f_*(\varepsilon_{f,F})\circ\eta_{f,f_*F}=\mathrm{id}_{f_*F}$ gives $\varepsilon_{f,F}(V\times_YX)(\eta_{f,f_*F}(V)(s))=s$ in $F(V\times_YX)$; taking germs at $(V\times_YX,(\bar v,\bar x))$ and using the germ property of $c$, both sides agree on the germ of $\eta(V)(s)$, and these germs are all of $(f^{-1}f_*F)_{\bar x}$ because $c$ is bijective and sends them onto all germs of $(f_*F)_{\bar y}$.)
