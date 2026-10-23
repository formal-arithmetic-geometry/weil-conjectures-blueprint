+++
id = "sk-d-ab-tate"
kind = "definition"
title = "Integral and rational Tate modules"
lean = ["AddCommGroup.tateModule", "AddCommGroup.rationalTateModule", "AddCommGroup.tateModule.instModule", "AddCommGroup.rationalTateModule.exists_eq_inv_pow_tmul", "AddCommGroup.rationalTateModule.inv_pow_tmul_eq_inv_pow_tmul_iff", "AddCommGroup.tateModule.map", "AddCommGroup.rationalTateModule.map", "AddCommGroup.rationalTateModule.fixedSubmodule", "AlgebraicGeometry.IsAbelianVariety.tateModule", "AlgebraicGeometry.IsAbelianVariety.rationalTateModule"]
order = 491
uses = ["sk-d-ab-field"]
tags = ["sketch"]
+++
For the prime $\ell$ and an abelian group $M$, put

$$
M[\ell^n]=\{x:\ell^nx=0\},\qquad
T_\ell M=\{(t_n)_{n\ge1}:t_n\in M[\ell^n],\ \ell t_{n+1}=t_n\}.
$$

The ring $\Zell$ consists of compatible residues
$c_n\in\mathbf Z/\ell^n\mathbf Z$ under reduction.
It acts by $(ct)_n=c_nt_n$, independently of the integer representative
of $c_n$. Define $\Qell=\Zell[1/\ell]$ and
$V_\ell M=T_\ell M[1/\ell]$. A fraction is written $\ell^{-b}t$;
the equality of fractions $\ell^{-b}t=\ell^{-c}u$ means that
$\ell^d(\ell^ct-\ell^bu)=0$ for some $d\ge0$.
An automorphism $s$ of $M$ acts coordinatewise and on fractions, and
$(V_\ell M)^s$ denotes its fixed submodule. For
an abelian variety, write $T_\ell A,V_\ell A$.
