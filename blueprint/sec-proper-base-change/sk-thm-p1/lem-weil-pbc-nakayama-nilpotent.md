+++
id = "lem-weil-pbc-nakayama-nilpotent"
kind = "lemma"
title = "Nakayama's lemma for a nilpotent ideal (surjectivity modulo I)"
lean = ["RingTheory.surjective_of_surjective_mod_nilpotent"]
source = "literature/stacks-project/algebra.tex, Algebra, Lemma 00DV (label lemma-NAK, Nakayama's lemma), part (11); proof: 'Part (9) holds because if M = IM then M = I^nM for all n and I being nilpotent means I^n = 0 for some n; Parts (10), (11), and (12) follow from (9) by the arguments used above' (i.e. (11) from (10) applied to the submodules Im(N -> M) and M, (10) from (9) applied to M/N)"
+++
Let $R$ be a commutative ring, $I\subseteq R$ a nilpotent ideal ($I^k=0$ for some $k\ge1$), and $u:N\to M$ a homomorphism of $R$-modules (no finiteness assumed on $N$ or $M$). If the induced map $N/IN\to M/IM$ is surjective, i.e. $M=u(N)+IM$, then $u$ is surjective. (Equivalently, parts (9)-(10) of the source: if $M=IM$ then $M=0$; if $N,N'\subseteq M$ are submodules with $M=N+IN'$, then $M=N$.)
