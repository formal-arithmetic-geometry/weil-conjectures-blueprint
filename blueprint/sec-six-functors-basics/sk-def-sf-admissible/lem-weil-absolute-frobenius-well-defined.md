+++
id = "lem-weil-absolute-frobenius-well-defined"
kind = "lemma"
title = "The Frobenius of the structure sheaf is a morphism of locally ringed spaces; affine case"
order = 2662
uses = ["def-weil-ring-frobenius", "def-weil-scheme-characteristic-p", "def-weil-locally-ringed-space-morphism", "def-weil-affine-spectrum", "def-pc-scheme"]
tags = ["stacks-0CC6"]
+++
Let $p$ be a prime number. (i) Let $A$ be a commutative ring with $p\cdot1=0$ and $F_A:A\to A$, $a\mapsto a^p$, its Frobenius endomorphism. For every prime ideal $\mathfrak p\subseteq A$, $F_A^{-1}(\mathfrak p)=\mathfrak p$; hence the continuous map of $\operatorname{Spec}(F_A):\operatorname{Spec}A\to\operatorname{Spec}A$ is the identity. (ii) If moreover $A$ is local, $F_A$ is a local homomorphism. (iii) Let $X$ be a scheme with $p=0$ in $\mathcal O_X$. The maps $F_{\mathcal O_X(U)}$, $U\subseteq X$ open, form an endomorphism $F^\sharp$ of the sheaf of rings $\mathcal O_X$ whose map on the stalk at $x$ is $F_{\mathcal O_{X,x}}$; consequently $(\mathrm{id}_X,F^\sharp):X\to X$ is a morphism of locally ringed spaces, hence an endomorphism of the scheme $X$. (iv) If $X=\operatorname{Spec}A$ with $p=0$ in $A$, this endomorphism equals $\operatorname{Spec}(F_A)$; more generally, for an open subscheme $U\subseteq X$ the endomorphism $(\mathrm{id}_X,F^\sharp)$ restricts to the corresponding endomorphism of $U$, and for an affine open $U\cong\operatorname{Spec}A$ that restriction is $\operatorname{Spec}(F_A)$. The same holds for the iterates, with $a\mapsto a^{p^n}$.
