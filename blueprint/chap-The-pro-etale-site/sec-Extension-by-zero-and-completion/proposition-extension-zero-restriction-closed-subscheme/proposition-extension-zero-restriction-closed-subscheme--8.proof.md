+++
kind = "proof"
of = "proposition-extension-zero-restriction-closed-subscheme--8"
order = 201017
uses = ["proposition-pro-etale-affines-form-basis", "definition-ind-etale-pro-etale-weakly--1", "definition-ind-etale-pro-etale-weakly--2", "proposition-etale-implications--1", "lemma-stability--6", "lemma-stability--7", "lemma-stability--8", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--1", "proposition-pro-etale-affines-form-basis--1", "proposition-pro-etale-affines-form-basis--2"]
+++
*Step 2: exactness of $j^*$ and $j_!$.* The functor $j^*$ is
restriction to $U_{\mathrm{pro}\acute{e}t}$, hence exact. The functor $j_!$ is exact
because its composites $j^*j_!$ and $i^*j_!$ are exact and the pair
$(j^*,i^*)$ detects exactness. The first composite is $j^*j_!=\mathrm{id}$.
The second is $i^*j_!=0$. Indeed, in the localization sequence of $j_!N$
the first map $j_!j^*j_!N\to j_!N$ is an isomorphism since $j^*j_!N=N$.
Hence $i_*i^*j_!N=0$, and $i^*j_!N=0$ because $i_*$ is fully faithful. The pair
$(j^*,i^*)$ detects exactness, because both functors are exact, hence
commute with taking homology of a complex of sheaves, while a sheaf $M$
with $j^*M=0$ and $i^*M=0$ is zero by the localization sequence.

*Source:* the proof of Proposition [proposition-extension-zero-restriction-closed-subscheme].
