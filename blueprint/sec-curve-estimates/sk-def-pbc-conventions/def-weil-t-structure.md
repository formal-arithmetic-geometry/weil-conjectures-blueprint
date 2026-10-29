+++
id = "def-weil-t-structure"
kind = "definition"
title = "t-structure"
order = 1359
lean = ["CategoryTheory.Triangulated.TStructure", "CategoryTheory.Triangulated.TStructure.heart", "CategoryTheory.Triangulated.TStructure.bounded", "CategoryTheory.Triangulated.TStructure.truncLE", "CategoryTheory.Triangulated.TStructure.truncGE", "CategoryTheory.Triangulated.TStructure.triangleLEGE"]
+++
A *t-structure* on a triangulated category $\mathcal T$ is a pair $(\mathcal
T^{\le0},\mathcal T^{\ge0})$ of strictly full subcategories such that

1. $\mathcal T^{\le0}[1]\subseteq\mathcal T^{\le0}$ and $\mathcal
   T^{\ge0}[-1]\subseteq\mathcal T^{\ge0}$;
2. $\Hom_{\mathcal T}(A,B[-1])=0$ for all $A\in\mathcal T^{\le0}$ and
   $B\in\mathcal T^{\ge0}$;
3. every $K\in\mathcal T$ occurs in a distinguished triangle $A\to K\to
   B[-1]\to A[1]$ with $A\in\mathcal T^{\le0}$ and $B\in\mathcal T^{\ge0}$.

Write $\mathcal T^{\le n}=\mathcal T^{\le0}[-n]$ and $\mathcal T^{\ge
n}=\mathcal T^{\ge0}[-n]$. The *heart* is $\mathcal T^{\le0}\cap\mathcal
T^{\ge0}$. An object is *bounded* if it lies in
$\mathcal T^{\le n}\cap\mathcal T^{\ge m}$ for some $m\le n$, and the
t-structure is *bounded* if every object of $\mathcal T$ is bounded.
Every t-structure carries truncation functors $\tau^{\le n},\tau^{\ge
n}:\mathcal T\to\mathcal T$ and distinguished truncation triangles

$$
 \tau^{\le n}K\longrightarrow K\longrightarrow
 \tau^{\ge n+1}K\longrightarrow\tau^{\le n}K[1],
$$

characterized by $\tau^{\le n}K\in\mathcal T^{\le n}$ and $\tau^{\ge
n+1}K\in\mathcal T^{\ge n+1}$.
