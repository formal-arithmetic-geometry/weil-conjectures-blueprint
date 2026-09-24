+++
id = "lem-weil-pbc-pushout-monomorphism"
kind = "lemma"
title = "Pushout monomorphism"
order = 1737
uses = ["def-weil-pbc-etale-sheaves"]
+++
If $A\hookrightarrow B$ and $A\hookrightarrow C$ are monomorphisms of etale
sheaves, then the canonical map

$$
 C\longrightarrow B\amalg_AC
$$

is a monomorphism.

## Proof

In the abelian category of etale sheaves, the pushout $B\amalg_AC$ is the
cokernel of $(a,-a'):A\to B\oplus C$. If the class of $(0,c)$ is zero, locally
on the site it equals $(a(x),-a'(x))$ for some section $x$ of $A$. Since $a$
is a monomorphism, $a(x)=0$ implies $x=0$, and then $c=0$. Thus the kernel
sheaf of $C\to B\amalg_AC$ is zero.
