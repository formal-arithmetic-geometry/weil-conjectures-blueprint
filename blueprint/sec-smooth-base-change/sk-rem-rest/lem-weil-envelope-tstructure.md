+++
id = "lem-weil-envelope-tstructure"
kind = "lemma"
title = "The envelope inherits the t-structure"
order = 1479
uses = ["def-weil-karoubi-envelope", "def-weil-t-structure", "lem-weil-karoubi-envelope-triangulated"]
+++
Let $\mathcal T$ be a triangulated category with a t-structure $(\mathcal
T^{\le0},\mathcal T^{\ge0})$, and let $(\Kar\mathcal T)^{\le0}$ and
$(\Kar\mathcal T)^{\ge0}$ be the closures under retracts of the images of
$\mathcal T^{\le0}$ and $\mathcal T^{\ge0}$ in the Karoubi envelope $\mathcal
T^\natural=\Kar(\mathcal T)$ of [def-weil-karoubi-envelope]. These form a
t-structure on $\mathcal T^\natural$, the truncation triangle of an object
$(K,e)$ being

$$
 (\tau^{\le0}K,e_{\le0})\longrightarrow(K,e)\longrightarrow
 (\tau^{\ge1}K,e_{\ge1})\longrightarrow(\tau^{\le0}K,e_{\le0})[1],
$$

where $e_{\le0}=\tau^{\le0}(e)$ and $e_{\ge1}=\tau^{\ge1}(e)$. Its heart is
canonically equivalent to the Karoubi envelope $\Kar(\mathcal
T^{\le0}\cap\mathcal T^{\ge0})$ of the heart of $\mathcal T$.
