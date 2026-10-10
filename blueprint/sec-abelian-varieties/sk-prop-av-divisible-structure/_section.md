+++
id = "sk-prop-av-divisible-structure"
kind = "section"
title = "The torsion of a divisible group"
lean = ["AddSubgroup.nonempty_addEquiv_torsionBy_of_natCard_eq"]
order = 573
uses = ["sk-def-av"]
+++
*Proposition (sketch).*

Let $D$ be a divisible abelian group, $\ell$ a prime and $r\ge0$ with
$\lvert D[\ell]\rvert=\ell^r$. Then $D[\ell^n]\cong(\Z/\ell^n\Z)^r$
for every $n\ge0$.

## Proof

For $n=0$ both sides are trivial. For $n\ge1$ induct on $n$, the case
$n=1$ being the hypothesis $D[\ell]\cong(\Z/\ell\Z)^r$ (a group of
order $\ell^r$ killed by $\ell$). Multiplication by $\ell$ gives an exact
sequence
$0\to D[\ell]\to D[\ell^{n+1}]\xrightarrow{\ell}D[\ell^n]\to0$,
surjective on the right by divisibility. So $D[\ell^{n+1}]$ is a
finite abelian $\ell$-group of order $\ell^{(n+1)r}$ with
$\ell\cdot D[\ell^{n+1}]\cong(\Z/\ell^n\Z)^r$ and
$D[\ell^{n+1}][\ell]\cong(\Z/\ell\Z)^r$. Writing
$D[\ell^{n+1}]\cong\bigoplus_i\Z/\ell^{a_i}\Z$, the second condition
says there are exactly $r$ cyclic summands and the first that exactly
$r$ of them satisfy $a_i\ge2$ with $a_i-1=n$; hence all $a_i=n+1$.
