+++
id = "det-p-cyclotomic"
kind = "proposition"
title = "Cyclotomic Frobenius"
lean = ["cyclotomicCharacter_frobeniusEquiv_pow", "cyclotomicCharacter_frobeniusEquiv_pow_inv_mul"]
order = 3822
uses = ["det-d-ab-cyclotomic", "sk-d-ab-field", "sk-d-ab-tate"]
+++
Let $\bar k$ be an algebraically closed field of characteristic $p$,
let $q=p^a$ with $a\ge0$, and let $\ell\ne p$ be a prime. On the
cyclotomic Tate module $\Zell(1)$ of $\bar k$, the $q$-power arithmetic
Frobenius $x\mapsto x^q$ acts as multiplication by
$q$, and the geometric Frobenius, its inverse, acts as multiplication by
$q^{-1}\in\hyperref[sk-d-ab-tate]{\Zell}^{\times}$.
