+++
id = "lem-weil-pbc-free-sheaf-flat"
kind = "lemma"
title = "The sheafified free presheaf on a representable with flat coefficients is flat (j_{X!} of a constant flat sheaf is flat)"
uses = ["lem-weil-pbc-sheaf-tensor-closed"]
tags = ["stacks-03EV"]
+++
Let $\mathcal C$ be an essentially small category with a Grothendieck topology $J$, and let $\mathcal A$ be a Grothendieck abelian category with a symmetric monoidal closed structure whose tensor product is additive in each variable; give $\mathrm{Sh}(\mathcal C,J;\mathcal A)$ the sheafified objectwise tensor product. Let $P$ be an object of $\mathcal A$ such that $P\otimes-:\mathcal A\to\mathcal A$ preserves finite limits, let $X$ be an object of $\mathcal C$, and let $P_X^\#$ be the sheaf associated to the presheaf $V\mapsto\bigoplus_{\varphi\in\mathrm{Mor}_{\mathcal C}(V,X)}P$ (restriction along $\psi:V'\to V$ sending the summand of $\varphi$ to that of $\varphi\psi$ by the identity); equivalently $P_X^\#=j_{X!}\underline P_X$, the extension by zero of the constant sheaf $P$ on $\mathcal C/X$. Then $P_X^\#\otimes-:\mathrm{Sh}(\mathcal C,J;\mathcal A)\to\mathrm{Sh}(\mathcal C,J;\mathcal A)$ preserves finite limits.
