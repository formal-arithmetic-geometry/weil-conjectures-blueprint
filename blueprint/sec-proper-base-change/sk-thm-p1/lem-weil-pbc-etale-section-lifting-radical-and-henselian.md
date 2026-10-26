+++
id = "lem-weil-pbc-etale-section-lifting-radical-and-henselian"
kind = "lemma"
title = "Radical and root-lifting consequences of etale section lifting"
uses = ["def-weil-pbc-henselian-terminology"]
lean = ["etale_section_lifting_radical_and_henselian"]
order = 1725
+++
Let $A$ be a commutative ring and $I\subseteq A$ an ideal such that étale sections lift along $A\to A/I$: for every étale $A$-algebra $A'$ and every $A$-algebra homomorphism $\sigma:A'\to A/I$ there is an $A$-algebra homomorphism $\tau:A'\to A$ whose composite with $A\to A/I$ is $\sigma$. Then $I$ is contained in the Jacobson radical of $A$, and the pair $(A,I)$ is henselian [def-weil-pbc-henselian-terminology]: for every monic $f\in A[T]$ and every $a_0\in A$ with $f(a_0)\in I$ and $f'(a_0)$ a unit modulo $I$, there is $a\in A$ with $f(a)=0$ and $a-a_0\in I$.
