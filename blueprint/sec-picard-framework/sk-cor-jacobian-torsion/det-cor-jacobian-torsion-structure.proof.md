+++
kind  = "proof"
of    = "det-cor-jacobian-torsion-structure"
uses = ["det-cor-jacobian-torsion-kernel", "lem-sc-av-commutative", "lem-sc-divisible-group-structure", "sk-thm-picard-main"]
+++
The group $A(k)$ is commutative ([lem-sc-av-commutative]), so every
$A(k)[m]$ is a finite abelian group, of order $m^{2g}$ for $m$ invertible
in $k$ by [det-cor-jacobian-torsion-kernel] (2).

*Prime-power part.* Let $q$ be a prime dividing $n$ and let $q^a$ be the
exact power of $q$ dividing $n$; then $q$ and $q^a$ are invertible in $k$.
The group $G=A(k)[q^a]$ has order $q^{2ga}$ and is killed by $q^a$. By the
classification of finite abelian groups,
$G\simeq\bigoplus_{i=1}^s\Z/q^{e_i}\Z$ with $1\le e_i\le a$. The subgroup
of $G$ killed by $q$ is $A(k)[q]$, of order $q^{2g}$; on the other hand it
is $\bigoplus_i q^{e_i-1}\Z/q^{e_i}\Z\simeq(\Z/q\Z)^s$, of order $q^s$.
Hence $s=2g$. Comparing orders, $\sum_{i=1}^{2g}e_i=2ga$ with every
$e_i\le a$, which forces $e_i=a$ for all $i$. Thus
$A(k)[q^a]\simeq(\Z/q^a\Z)^{2g}$. (Equivalently, since $A(k)$ is
divisible, this is [lem-sc-divisible-group-structure] with $r=2g$.)

*Combining primes.* Write $n=\prod_qq^{a_q}$. A finite abelian group killed
by $n$ is the direct sum of its $q$-primary parts, and the $q$-primary part
of $A(k)[n]$ is $A(k)[q^{a_q}]$. Hence
$$
A(k)[n]=\bigoplus_{q\mid n}A(k)[q^{a_q}]\simeq\bigoplus_{q\mid n}(\Z/q^{a_q}\Z)^{2g}\simeq(\Z/n\Z)^{2g},
$$
the last step by the Chinese remainder theorem
$\Z/n\Z\simeq\prod_q\Z/q^{a_q}\Z$.

*Non-canonicity.* Two isomorphisms $\phi,\psi\colon A(k)[n]\to(\Z/n\Z)^{2g}$
differ by $\psi\circ\phi^{-1}\in\mathrm{GL}_{2g}(\Z/n\Z)$, and every element
of this group arises; the construction above involves choosing cyclic
decompositions, so it singles out no element.

For $A=J(C)$, which is an abelian variety of dimension $g$ by
[sk-thm-picard-main], this gives $J(C)[n](k)\simeq(\Z/n\Z)^{2g}$.
