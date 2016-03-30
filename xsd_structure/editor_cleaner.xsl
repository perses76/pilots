<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns="rebelrunner_unformatted.xsd" 
    >
    <xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>


    <xsl:template match="/">
        <skeleton>
            <not_allowed/>
            <xsl:apply-templates select="@*|node()"/>
        </skeleton>
    </xsl:template>

    <xsl:template match="*">
        <xsl:element name="{name()}">
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="@*">
        <xsl:copy />
    </xsl:template>

    <xsl:template match="block[@name='Footer']">
        <Footer strong_type_block="true">
            <xsl:apply-templates />
        </Footer>
    </xsl:template>

    <xsl:template match="posts">
        <xsl:element name="{name()}">
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="list | list_item | link">
        <xsl:element name="{name()}">
            <xsl:apply-templates select="@*|node()"/>
        </xsl:element>
    </xsl:template>

    <xsl:template match="@removable"></xsl:template>
    <xsl:template match="comment"></xsl:template>

</xsl:stylesheet>
