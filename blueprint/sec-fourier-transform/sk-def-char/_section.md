+++
id = "sk-def-char"
kind = "section"
title = "Additive characters"
order = 2671
lean = ["AddChar.FiniteField.primitiveChar"]
uses = ["sk-def-fourier-set"]
+++
*Definition (sketch).*

A *nondegenerate additive character* of $k$ (finite or algebraically
closed of characteristic $p$) is a nontrivial homomorphism
$\psi:(k,+)\to\Qlb^\times$. For $k_0=\Fq$, a field $F'$ of characteristic
$\neq p$ (for instance $\Qlb$) and a fixed nontrivial character
$\Psi:\Fp\to F'(\mu_p)^\times$ with values in the $p$-th cyclotomic
extension of $F'$, the character $\psi(x)=\Psi(\Tr_{k_0/\Fp}(x))$ is *the*
nondegenerate additive character; it is primitive: $\psi_a(x)=\psi(ax)$ is
nontrivial for every $a\in k_0^\times$. Over $\mathbf F_{q^n}$ one writes
$\psi_n(x)=\psi(\Tr_{\mathbf F_{q^n}/k_0}(x))=\Psi(\Tr_{\mathbf F_{q^n}/\Fp}(x))$.
