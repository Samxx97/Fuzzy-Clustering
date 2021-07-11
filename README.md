<h1 align="center"> Fuzzy Clustering </h1>

<h2 id="Description"> :book: Description</h2>



<p align="justify">
 a Numpy vectorized implementation written in Python of some of the fuzzy clustering algorithms which includes the following:
 </p>
 
<ul>
<li> ➤ Fuzzy C-Means:  </li>
<li> ➤	Gustafason-Kessel:  </li>
</ul>

<h3> Theoritical Generlized Description of the Fuzzy Algorithm </h3>

<p> Fuzzy Clustering is a form of clustering in which each data point can belong to more than one cluster it involves assigning data points to clusters such that items in the same cluster are as similar as possible while items belonging to different clusters are as dissimiliar as possible.Clusters are identified via similarity measures.Different similarity measures may be used, in this implementation the euclidean distance and  Mahalanobis distance are used.
</p>

<h3> Comparison to hard Clustering </h3>
<p> 
in non-fuzzy clustering, data is divided into distinct clusters, where each data point can only belong to exactly one cluster.In Fuzzy clustering can potentially belong to multiple clusters.
</p>

<h3> The Algorithm: </h3>

<ol>
<li> Initialize Membership Matrix such that values across each center sum to 1</li>
<li> Update the Class Centers Matrix</li>
<li> Calculate the distances of samples from Class Centers</li>
<li> Update Memberships</li>
<li> Repeat step number 2 Until Convergence or reaching maximum number of iterations allowed</li>
</ol>

