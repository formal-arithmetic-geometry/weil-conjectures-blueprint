+++
id = "def-weil-absolute-frobenius-scheme"
kind = "definition"
title = "Absolute q-power Frobenius of a scheme in characteristic p"
order = 2644
uses = ["def-pc-scheme", "def-weil-scheme-characteristic-p", "def-weil-locally-ringed-space-morphism", "def-weil-ring-frobenius", "lem-weil-absolute-frobenius-well-defined", "def-weil-affine-spectrum"]
tags = ["stacks-0CC6"]
+++
Let $p$ be a prime number and let $X$ be a scheme [def-pc-scheme] of characteristic $p$ [def-weil-scheme-characteristic-p], i.e. $p=0$ in $\mathcal O_X$. The *absolute Frobenius* of $X$ is the morphism of schemes $F_X:X\to X$ that is the identity on the underlying topological space and whose map of structure sheaves [def-weil-locally-ringed-space-morphism] $F_X^\sharp:\mathcal O_X\to\mathcal O_X$ is $g\mapsto g^p$ on sections over every open set, i.e. the Frobenius endomorphism [def-weil-ring-frobenius] of each ring $\mathcal O_X(U)$. (This is a morphism of locally ringed spaces because, for every ring $A$ of characteristic $p$, $a\mapsto a^p$ is a ring endomorphism of $A$ inducing the identity on $\operatorname{Spec}A$, and is a local homomorphism when $A$ is local [lem-weil-absolute-frobenius-well-defined].) For $q=p^a$ with $a\geq1$, the *absolute $q$-power Frobenius* of $X$ is the $a$-fold iterate (composite in the category of schemes)

$$
 \operatorname{Fr}^{(q)}_X=F_X^a:X\longrightarrow X,
$$

the identity on the underlying space with $g\mapsto g^q$ on $\mathcal O_X$; on an affine open $\operatorname{Spec}A\subseteq X$ it is $\operatorname{Spec}$ [def-weil-affine-spectrum] of the ring endomorphism $a\mapsto a^q$ of $A$ [lem-weil-absolute-frobenius-well-defined].
